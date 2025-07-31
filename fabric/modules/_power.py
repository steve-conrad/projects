import fabric
import os
import subprocess
from fabric.widgets.box import Box
from fabric.widgets.button import Button

class PowerMenu(Box):
    def __init__(self, **kwargs):
        super().__init__(
            vertical=True,
            name="power-menu",
            **kwargs
        )

        self.powerbutton = Button(
            label=" ",
            name="power-button"
        )
        self.powerbutton.connect("clicked", self.toggle_submenu)

        self.submenu = Box(
            vertical=True,
            name="power-submenu",
            children=[
                Button(label="Lock", name="lock-button"),
                Button(label="Restart", name="restart-button"),
                Button(label="Shutdown", name="shutdown-button"),
            ],
        )
        self.submenu.set_no_show_all(True)
        self.submenu.hide()

        self.add(self.powerbutton)
        self.add(self.submenu)

    def toggle_submenu(self, *args):
        if self.submenu.get_visible():
            self.submenu.hide()
        else:
            self.submenu.show()


