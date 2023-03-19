import csv


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, __name="", price=0.0, quantity=0):
        self.__name = __name
        self.price = price
        self.quantity = quantity
        self.all.append(self)
        if len(__name) > 10:
            raise NameError("Длина названия товара не должна превышать 10 символов!")

    def __repr__(self) -> str:
        text = ""
        for dic in self.__dict__:
            text += dic + "=" + str(self.__dict__[dic]) + ", "
        return f"Item({text[:-2]})"

    def calculate_amount(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price

    @classmethod
    def load_from_csv(cls, path) -> list:
        with open(path, "r", newline='') as csvfile:
            csv_data = csv.DictReader(csvfile)
            item_list = []
            for row in csv_data:
                item_list.append(cls(row['name'], int(row['price']), int(row['quantity'])))
            return item_list

    @staticmethod
    def is_integer(number) -> bool:
        return ((type(number) == int) or (type(number) == float)) \
            and (round(number) == number)
