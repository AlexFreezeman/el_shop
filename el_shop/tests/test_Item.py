from utils.item import Item


def test_calculate_amount(keyboard):
    assert keyboard.calculate_amount() == 12000
    item = Item("name", 50, 2)
    assert item.calculate_amount() == 100


def test_apply_discount(keyboard):
    keyboard.pay_rate = 0.8
    keyboard.apply_discount()
    assert keyboard.calculate_amount() == 0.8 * 12000.0
