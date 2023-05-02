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

    def __repr__(self) -> str:
        text = "Item("
        for dic in self.__dict__:
            text += f'{dic}={self.__dict__[dic]}, '
        return f"{text[:-2]})"

    def __str__(self) -> str:
        return f"Товар: {self.__name}, цена: {self.price}, количество: {self.quantity}"


class Phone(Item):
    def __init__(self, name="", price=0.0, quantity=0, number_of_sim=1):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim
        self.name = name
        if number_of_sim == 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    @staticmethod
    def add_item(data1, data2):
        if (isinstance(data1, Phone) or isinstance(data1, Item)) and \
                (isinstance(data2, Phone) or isinstance(data2, Item)):
            return data1.quantity + data2.quantity
        else:
            raise (ValueError, "Объекты должны быть типа Phone или Item")

    def __repr__(self) -> str:
        text = "Phone("
        for dic in self.__dict__:
            text += f'{dic}={self.__dict__[dic]}, '
        return f"{text[:-2]})"

    def __str__(self) -> str:
        return f"Телефон: {self.name}, цена: {self.price}, количество: {self.quantity}, количество сим-карт: {self._number_of_sim}"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number: int):
        if isinstance(number, int) and number > 0:
            self._number_of_sim = number
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
