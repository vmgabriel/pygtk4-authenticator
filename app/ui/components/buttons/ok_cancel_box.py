import dataclasses

from typing import Any

from app.ui import gtk
from app.ui.components.buttons import box_buttons


class OkCancelButtonsBox(box_buttons.ButtonsBox):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._box = gtk.Gtk.Box(spacing=5, orientation=gtk.Gtk.Orientation.HORIZONTAL)
        self._box.props.homogeneous = True

        buttons = [
            box_buttons.Button(event_name="ACCEPT", title="Aceptar"),
            box_buttons.Button(event_name="CANCEL", title="Cancelar"),
        ]

        super().__init__(buttons=buttons, *args, **kwargs)