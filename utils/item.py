class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name="", price=0.0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def calculate_amount(self):
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate
