import pytest
from utils.item import Phone


def test_add_item(the_phone,  keyboard):
    assert the_phone.add_item(the_phone, keyboard) == 15
    with pytest.raises(TypeError):
        the_phone.add_item(the_phone, 2)


def test__init__():
    assert Phone("iPhone 14", 120_000, 5, 2).name == "iPhone 14"
    with pytest.raises(ValueError):
        Phone("The Phone", 1000, 10, 0)


def test__repr__(the_phone) -> str:
    assert repr(the_phone) == "Phone(_Item__name=The Phone, price=1000, quantity=10, _number_of_sim=1)"


def test__str__(the_phone) -> str:
    assert str(the_phone) == "Телефон: The Phone, цена: 1000, количество: 10, количество сим-карт: 1"


def test_number_of_sim(the_phone):
    assert the_phone.number_of_sim == 1
    phone = Phone("iPhone 14", 120_000, 5, 4)
    phone.number_of_sim = 4
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
    with pytest.raises(ValueError):
        phone.number_of_sim = -1
    with pytest.raises(ValueError):
        phone.number_of_sim = 0.5