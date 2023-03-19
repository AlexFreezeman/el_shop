import pytest
import os
from utils.item import Item


@pytest.fixture()
def keyboard():
    keyboard = Item("клавиатура", 2400, 5)
    return keyboard


#@pytest.fixture()
#def path_csv_file():
#    return os.sep.join(["tests", "items.csv"])
