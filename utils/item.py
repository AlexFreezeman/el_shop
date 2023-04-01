import csv


class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, __name="", price=0.0, quantity=0):
        self.__name = __name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            raise Exception("Длина названия товара превышает 10 символов.")
        else:
            self.__name = value

    def calculate_amount(self):
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price = self.price * self.pay_rate

    @staticmethod
    def is_integer(number) -> bool:
        return ((type(number) == int) or (type(number) == float)) \
               and (round(number) == number)

    @classmethod
    def instantiate_from_csv(cls, path_csv) -> None:
        with open(path_csv, "r", newline="") as file:
            csv_data = csv.DictReader(file)
            item_list = []
            for row in csv_data:
                item_list.append(cls(row['name'], int(row['price']), int(row['quantity'])))
