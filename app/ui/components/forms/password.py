from typing import Any

from app.ui import gtk
from app.ui.components.forms import component
from app.ui.components import component as base_component

class PasswordForm(component.FieldForm):
    _label: gtk.Gtk.Label
    _pass: gtk.Gtk.PasswordEntry

    def __init__(self, label: str, placehoder_text: str = "Password") -> None:
        margins = base_component.Margins(
            left=10,
            right=10,
            top=10,
        )

        super().__init__(margins=margins)

        self._box = gtk.Gtk.Box(spacing=5, orientation=gtk.Gtk.Orientation.HORIZONTAL)
        
        # label
        self._label = gtk.Gtk.Label(label=label)
        self._label.props.halign = gtk.Gtk.Align.START
        self._box.append(self._label)

        # password
        self._pass = gtk.Gtk.PasswordEntry()
        self._pass.props.placeholder_text = placehoder_text
        self._pass.props.show_peek_icon = True
        self._box.append(self._pass)

        # Buttons Box

    def _value(self) -> Any:
        return self._pass.get_text()

    def clear(self) -> None:
        self._pass.set_text("")

    def focus(self) -> None:
        self._pass.grab_focus_without_selecting()
