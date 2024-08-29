from collections.abc import MutableSequence

from dash.dependencies import Component

SingleChild = None | str | float | Component
Child = SingleChild | MutableSequence[SingleChild] | tuple[SingleChild]
