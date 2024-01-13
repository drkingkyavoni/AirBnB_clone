#!/usr/bin/env python3


from ...models.base_model import BaseModel
from ...models.state import State


def test_state_initialization():
    """
    Test the initialization of the state object.

    This function creates a state object with a specified name and asserts that
    the name attribute of the state object is equal to the specified name.

    Parameters:
        None

    Returns:
        None
    """
    state = State(name="Test State")
    assert state.name == "Test State"


def test_state_base_model_inheritance():
    """
    Test the inheritance of the State class from the BaseModel class.

    This function creates an instance of the State class and checks if it is an
    instance of the BaseModel class.

    Returns:
        None
    """
    state = State()
    assert isinstance(state, BaseModel)
