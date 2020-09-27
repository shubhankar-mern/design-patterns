from component import Component
from dataclasses import dataclass


@dataclass
class Decorator(Component):
    """
    The base Decorator class follows the same interface as the other components.
    The primary purpose of this class is to define the wrapping interface for
    all concrete decorators. The default implementation of the wrapping code
    might include a field for storing a wrapped component and the means to
    initialize it.
    """

    _component: Component

    @property
    def component(self) -> Component:
        """The Decorator delegates all work to the wrapped component."""
        return self._component

    def operation(self) -> str:
        return self._component.operation()