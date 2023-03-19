import pytest
import pytest_cov
from utils.item import Item


def test__init__(keyboard):
    assert keyboard._Item__name == "клавиатура"
    assert keyboard.price == 2400
    assert keyboard.quantity == 5
    with pytest.raises(NameError, match="Длина названия товара не должна превышать 10 символов!"):
        item = Item("очень длинное имя", 1, 1)


def test_calculate_amount(keyboard):
    assert keyboard.calculate_amount() == 12000
    item1 = Item("name", 50, 2)
    assert item1.calculate_amount() == 100


def test_apply_discount(keyboard):
    assert keyboard.pay_rate == 1
    item1 = Item("name", 50, 2)
    item1.pay_rate = 0.8
    assert item1.apply_discount() == 40.0
    assert item1.price == 40
    assert int(item1.calculate_amount()) == 80


def test_is_integer():
    item = Item("name", 50, 2)
    assert item.is_integer(5) is True
    assert item.is_integer(5.0) is True
    assert item.is_integer(5.5) is False
    assert item.is_integer("5") is False


def test__repr__(keyboard):
    assert str(keyboard) == "Item(_Item__name=клавиатура, price=2400, quantity=5)"


# def test_load_from_csv(path_csv_file) -> list:
#    item = Item("name", 50, 2)
#    assert len(item.load_from_csv(path_csv_file)) == 5
#    assert isinstance(item.load_from_csv(path_csv_file)[0], Item)
