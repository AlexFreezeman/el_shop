import pytest
from utils.item import Item


@pytest.fixture()
def keyboard():
    keyboard = Item("клавиатура", 2400, 5)
    return keyboard


@pytest.fixture(autouse=True)
def clear_items():
    Item.all = []
