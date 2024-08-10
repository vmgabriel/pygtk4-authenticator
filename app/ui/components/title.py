import abc

from typing import Any

from app.ui import gtk
from app.ui.components import component


_DEFAULT_FONT = component.Font(
    name="Ubuntu",
    size=30000,
)


class Title(component.Component):
    _label: gtk.Gtk.Label

    def __init__(
        self,
        title: str,
        font: component.Font = _DEFAULT_FONT,
        *args: Any, **kwargs: Any
    ) -> None:
        super().__init__(*args, **kwargs)

        self._box = gtk.Gtk.Box(orientation=gtk.Gtk.Orientation.HORIZONTAL)

        # label
        self._label = gtk.Gtk.Label(label="")
        self._label.set_markup("<span size='{size}'>{title}</span>".format(size=font.size, title=title))
        self._box.append(self._label)
