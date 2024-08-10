from typing import Any

from app.ui import gtk
from app.ui.components import title, component


class HomeWindow(gtk.Gtk.ApplicationWindow):
    def __init__(self, **kargs: Any):
        super().__init__(
            **kargs,
            title="Home",
        )

        # box
        main_box = gtk.Gtk.Box(
            spacing=6,
            orientation=gtk.Gtk.Orientation.VERTICAL,
        )
        self.set_child(main_box)
        self.set_resizable(False)

        margin_title = component.Margins(top=40, bottom=40, left=20, right=20)
        current_title = title.Title(title="Autenticado correctamente", margins=margin_title)
        current_title.build(main_box=main_box)
