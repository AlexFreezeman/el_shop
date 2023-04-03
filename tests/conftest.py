import pytest
import os
from utils.item import Item, Phone


@pytest.fixture()
def keyboard():
    keyboard = Item("клавиатура", 2400, 5)
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
