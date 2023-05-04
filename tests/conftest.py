import pytest
import os
from utils.item import Item, Phone
from utils.keyboard import KeyBoard, Mixin


@pytest.fixture()
def keyboard():
    keyboard = Item("KeyB", 2400, 5)
    return keyboard


@pytest.fixture(autouse=True)
def clear_items():
    Item.all = []


@pytest.fixture(autouse=True)
def path_csv():
    os.path.join('data', 'items.csv')


@pytest.fixture()
def the_phone():
    return Phone("The Phone", 1000, 10, 1)


@pytest.fixture()
def keyboard_test():
    return KeyBoard("KeyB", 2400, 5)


@pytest.fixture()
def mixin_test():
    return Mixin('EN')
