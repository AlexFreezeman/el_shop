import pytest
from utils.item import Item
from utils.config import path_csv


def test_calculate_amount(keyboard):
    assert keyboard.calculate_amount() == 12000
    item1 = Item("name", 50, 2)
    assert item1.calculate_amount() == 100


def test_apply_discount(keyboard):
    assert keyboard.pay_rate == 1
    item1 = Item("name", 50, 2)
    item1.pay_rate = 0.8
    assert item1.apply_discount() is None
    assert item1.price == 40
    assert int(item1.calculate_amount()) == 80


def test_all_items():
    item1 = Item("test_1", 10_000, 20)
    item2 = Item("test_2", 20_000, 5)

    assert Item.all == [item1, item2]


def test_name():
    item3 = Item("СуперВещь9999", 50000, 1)
    with pytest.raises(Exception):
        item3.name = "Длина названия товара превышает 10 символов."


def test_is_integer():
    item = Item("name", 1000, 5)
    assert item.is_integer(5) is True
    assert item.is_integer(5.0) is True
    assert item.is_integer(5.5) is False
    assert item.is_integer("5") is False


def test_instantiate_from_csv():
    Item.instantiate_from_csv("items.csv")
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[4].name == "Клавиатура"

