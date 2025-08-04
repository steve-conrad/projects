import fabric
from gi.repository import Gdk
from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.wayland import WaylandWindow as Window
from fabric.utils import get_relative_path, monitor_file

from modules._datetime import datetime
from modules._powerbutton import powerbutton
from modules._bluetooth import bluetooth
from modules._workspaces import workspaces
from modules._activewindow import activewindow
from modules._volume import VolumeWidget
from modules._network import network
from modules._notifications import notifications
from modules._power import PowerMenu

audio = VolumeWidget()
powermenu = PowerMenu()

class Bar(Window):
    def __init__(self, **kwargs):
        screen = Gdk.Screen.get_default()
        monitor_num = screen.get_primary_monitor()
        geometry = screen.get_monitor_geometry(monitor_num)
        monitor_width_px = geometry.width

        bar_scale = 0.6
        self.bar_width = int(monitor_width_px * bar_scale)
        self.bar_height = 30

        self.layout = self.build_layout()

        super().__init__(
            name="bar",
            layer="top",
            anchor="top",
            exclusivity="auto",
            child=self.layout,
            **kwargs,
        )

        self.set_size_request(self.bar_width, self.bar_height)
        self.show_all()

        display = Gdk.Display.get_default()
        display.connect("monitor-added", lambda *args: self.build_layout())

    def build_layout(self):
        start_box = Box(
            name="start-container",
            orientation="h",
            spacing=4,
            children=[powermenu, activewindow],
        )
        center_box = Box(
            name="center-container",
            orientation="h",
            spacing=4,
            children=[workspaces],
        )
        end_box = Box(
            name="end-container",
            orientation="h",
            spacing=4,
            children=[datetime, audio, bluetooth, network, notifications],
        )
        return CenterBox(
            name="center-bar",
            start_children=start_box,
            center_children=center_box,
            end_children=end_box,
        )

    def rebuild_layout(self):
        print(">> Rebuilding layout after monitor-added")

        # Remove old layout cleanly
        self.remove(self.layout)
        self.layout.destroy()

        # Build new layout and set as child
        self.layout = self.build_layout()
        self.set_child(self.layout)
        self.show_all()


if __name__ == "__main__":
    bar = Bar()
    app = Application("MenuBar", bar)

    def apply_stylesheet(*_):
        return app.set_stylesheet_from_file(
            get_relative_path("./styles/default.css")
        )

    style_monitor = monitor_file(get_relative_path("./styles/default.css"))
    style_monitor.connect("changed", apply_stylesheet)
    apply_stylesheet()

    app.run()

