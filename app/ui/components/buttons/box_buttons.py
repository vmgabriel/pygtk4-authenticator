import dataclasses

from typing import Any, List, Callable, Dict

from app.ui import gtk
from app.ui.components import component as base_component


@dataclasses.dataclass
class Button:
    event_name: str
    title: str


class ButtonsBox(base_component.Component):
    _callback: Callable
    _buttons: Dict[gtk.Gtk.Button, str]

    def __init__(self, buttons: List[Button], callback: Callable[str, None]) -> None:
        margins = base_component.Margins(
            left=10,
            right=10,
            top=30,
            bottom=20,
        )

        super().__init__(margins=margins)
        
        self._callback = callback
        self._buttons = {}

        for button in buttons:
            btn = gtk.Gtk.Button.new_with_label(button.title)
            btn.connect("clicked", self.event_click)
            self._buttons[btn] = button.event_name
            self._box.append(btn)

    def event_click(self, _button) -> None:
        self._callback(self._buttons[_button])
