from utils.item import Item, Phone
from utils.keyboard import KeyBoard
from utils.config import path_csv


def main():
    #    item1 = Item("Телефон", 10000, 5)
    #    item1.name = "Смартфон"
    #    print(item1.name)

    #   item2 = Item("Смартфон", 20000, 3) #вкл для проверки Exception
    #   item2.name = "СуперСмартфон" #вкл для проверки Exception

    # Item.instantiate_from_csv(path_csv)  # создание объектов из данных файла
    #    print(len(Item.all))  # в файле 5 записей с данными по товарам
    # item1 = Item.all[0]
    # print(item1)
    # print(Item.all)

    # print(item1.calculate_amount())
    #    print(item2.calculate_amount())
    # Item.pay_rate = 0.8

    # item1.apply_discount()

    # print(item1.price)
    #    print(item2.price)
    #    print(Item.all)

    # print(Item.is_integer(5))
    # print(Item.is_integer(5.0))
    # print(Item.is_integer(5.5))

    # смартфон iPhone 14, цена 120_000, количетсво товара 5, симкарт 2
#    phone1 = Phone("iPhone 14", 120_000, 5, 2)
#    print(phone1)
#    print(repr(phone1))
#    Phone('iPhone 14', 120000, 5, 2)
    # phone1.number_of_sim = 0

    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    # kb = KeyBoard('Dark', 9600, 5)
    print(kb)
    print(kb.language)
    kb.change_lang()
    print(kb.language)
    kb.change_lang()
    print(kb.language)
#    kb.language = 'CH'
    print(kb.__repr__())

if __name__ == "__main__":
    main()
