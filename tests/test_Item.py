from utils.item import Item


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


