import dataclasses

from typing import Any

from app.ui import gtk


@dataclasses.dataclass
class Margins:
    left: int = 0
    right: int = 0
    top: int = 0
    bottom: int = 0


@dataclasses.dataclass
class Font:
    name: str
    size: float

    def to_pango(self) -> gtk.Pango.FontDescription:
        return gtk.Pango.FontDescription(f"{self.name} {self.size}")


class Component(gtk.Gtk.Box):
    _box: gtk.Gtk.Box

    _margins: Margins

    def __init__(
        self, 
        margins: Margins = Margins(), 
        *args: Any, **kwargs: Any
    ) -> None:
        super().__init__(*args, **kwargs)

        self._margins = margins

    def _adjust_margins(self) -> None:
        self._box.props.homogeneous = True
        self._box.props.margin_start = self._margins.left
        self._box.props.margin_end = self._margins.right
        self._box.props.margin_top = self._margins.top
        self._box.props.margin_bottom = self._margins.bottom

    def build(self, main_box: gtk.Gtk.Box) -> None:
        self._adjust_margins()
        main_box.append(self._box)