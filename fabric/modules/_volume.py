from fabric.widgets.box import Box
from fabric.audio import Audio
from fabric.utils import cooldown
from fabric.widgets.eventbox import EventBox
from fabric.widgets.circularprogressbar import CircularProgressBar
from fabric.widgets.label import Label
from fabric.widgets.overlay import Overlay


class VolumeWidget(EventBox):
    def __init__(self, **kwargs):
        super().__init__(
            name="volume",
            events=["scroll", "smooth-scroll", "enter-notify-event"],
            **kwargs,
        )

        self.audio = Audio()

        self.box = Box(orientation="h", spacing=4)
        self.add(self.box) 

        self.progress_bar = CircularProgressBar(
            style_classes="overlay-progress-bar",
            pie=True,
            size=16,
        )

        self.icon = Label(
            label="󰕾", 
            style_classes="panel-font-icon overlay-icon",
        )

        self.box.add(
            Overlay(child=self.progress_bar, overlays=self.icon, name="overlay"),
        )

        self.audio.connect("notify::speaker", self.on_speaker_changed)
        self.connect("scroll-event", self.on_scroll)

        if True:
            self.volume_label = Label(style_classes="panel-text")
            self.box.add(self.volume_label)

    @cooldown(0.1)
    def on_scroll(self, _, event):
        val_y = event.delta_y
        step = self.config.get("step_size", 5)

        if val_y > 0:
            self.audio.speaker.volume += step
        else:
            self.audio.speaker.volume -= step

    def on_speaker_changed(self, *_):
        if not self.audio.speaker:
            return

        show_tooltip = False
        if show_tooltip:
            self.set_tooltip_text(self.audio.speaker.description)

        self.audio.speaker.connect("notify::volume", self.update_volume)
        self.update_volume()

    def toggle_mute(self):
        current_stream = self.audio.speaker
        if current_stream:
            current_stream.muted = not current_stream.muted
            self.icon.set_text("󰝟" if current_stream.muted else self.get_icon())

    def update_volume(self, *_):
        if not self.audio.speaker:
            return

        volume = round(self.audio.speaker.volume)
        self.progress_bar.set_value(volume / 100)

        if hasattr(self, "volume_label"):
            self.volume_label.set_text(f"{volume}%")

        self.icon.set_text(self.get_icon(volume, self.audio.speaker.muted))

    def get_icon(self, volume=None, muted=False):
        if muted:
            return "󰝟" 
        if volume is None:
            volume = round(self.audio.speaker.volume)
        if volume == 0:
            return "󰝝" 
        elif volume < 3:
            return "󰕿" 
        elif volume < 20:
            return "󰖀" 
        else:
            return "󰕾" 

