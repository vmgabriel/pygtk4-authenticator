from typing import Any

from app.ui import gtk
from app.ui.components import title as title_component, component


class DialogWindow(gtk.Gtk.ApplicationWindow):
    def __init__(self, title: str, message: str, **kargs: Any):
        super().__init__(
            **kargs,
            title=title,
        )

        self.set_resizable(False)

        # box
        main_box = gtk.Gtk.Box(
            spacing=6,
            orientation=gtk.Gtk.Orientation.VERTICAL,
        )
        self.set_child(main_box)
        self.set_resizable(False)

        margin_title = component.Margins(top=40, bottom=40, left=20, right=20)
        font_title = component.Font(name="Ubuntu", size=10000)
        current_title = title_component.Title(title=message, margins=margin_title, font=font_title)
        current_title.build(main_box=main_box)
