from typing import Any

from app.ui import gtk
from app.ui.components.forms import component
from app.ui.components import component as base_component


class InputForm(component.FieldForm):
    _label: gtk.Gtk.Label
    _entry: gtk.Gtk.Entry

    def __init__(self, label: str) -> None:
        margins = base_component.Margins(
            left=10,
            right=10,
            top=10,
        )

        super().__init__(margins=margins)

        self._box = gtk.Gtk.Box(spacing=5, orientation=gtk.Gtk.Orientation.HORIZONTAL)
        self._box.props.homogeneous = True
        
        # label
        self._label = gtk.Gtk.Label(label=label)
        self._label.props.halign = gtk.Gtk.Align.START
        self._box.append(self._label)

        # entry
        self._entry = gtk.Gtk.Entry()
        self._box.append(self._entry)

    def _value(self) -> Any:
        return self._entry.get_text()

    def clear(self) -> None:
        self._entry.set_text("")

    def focus(self) -> None:
        self._entry.grab_focus_without_selecting()
