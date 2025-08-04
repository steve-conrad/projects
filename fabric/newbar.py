import fabric
from fabric import Application
from fabric.widgets.box import Box
from fabric.widgets.label import Label
from fabric.widgets.button import Button
from fabric.widgets.datetime import DateTime
from fabric.widgets.centerbox import CenterBox
from fabric.widgets.wayland import WaylandWindow as Window

def create_button(): # define a "factory function"
    return Button(label="Click Me", on_clicked=lambda b, *_: b.set_label("you clicked me"))


class StatusBar(Window):
    def __init__(self, **kwargs):
        super().__init__(
            layer="top",
            anchor="left top right", 
            exclusivity="auto",
            **kwargs
        )

        self.date_time = DateTime()
        self.children = CenterBox(center_children=self.date_time)

if __name__ == "__main__":
    bar = StatusBar()
    app = Application("Hyprnosis-bar", bar)
    app.run()
