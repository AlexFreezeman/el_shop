import pytest
from utils.keyboard import KeyBoard, Mixin


def test_mixin__init__(mixin_test):
    assert mixin_test._language == "EN"
    key_mixin = Mixin()
    assert key_mixin._language == "EN"


def test_mixin_setter():
    key_mixin = Mixin()
    with pytest.raises(AttributeError):
        key_mixin.language = "PL"


def test_mixin_change_lang():
    key_mixin = Mixin()
    key_mixin.change_lang()
    assert key_mixin._language == "RU"
    key_mixin.change_lang()
    assert key_mixin._language == "EN"


def test_keyboard_init(keyboard_test):
    keyboard = KeyBoard("KeyB", 2400, 5)
    assert keyboard._Item__name == keyboard_test._Item__name
    assert keyboard.price == keyboard_test.price
    assert keyboard.quantity == keyboard_test.quantity
    assert keyboard.language == keyboard_test.language


def test_keyboard_change_lang():
    keyboard = KeyBoard("KeyB", 2400, 5)
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == "EN"


def test_keyboard__repr__(keyboard_test):
    assert repr(keyboard_test) == "KeyBoard(_Item__name="", price=2400, quantity=5, _language=EN, _KeyBoard__name=KeyB)"


def test_keyboard__str__(keyboard_test):
    assert str(keyboard_test) == "Клавиатура: KeyB, цена: 2400, количество: 5"