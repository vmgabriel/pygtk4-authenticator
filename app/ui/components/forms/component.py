import abc

from typing import Any

from app.ui import gtk
from app.ui.components import component


class FieldForm(component.Component):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    @property
    def value(self) -> Any:
        return self._value()

    @abc.abstractmethod
    def _value(self) -> Any:
        raise NotImplementedError()

    @abc.abstractmethod
    def clear(self) -> None:
        raise NotImplementedError()