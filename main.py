from utils.item import Item
from utils.config import path_csv


def main():
    item1 = Item("Телефон", 10000, 5)
    item1.name = "Смартфон"
    print(item1.name)

    item2 = Item("Смартфон", 20000, 3)
#    item2.name = "СуперСмартфон"

    Item.instantiate_from_csv(path_csv)  # создание объектов из данных файла
    print(len(Item.all))  # в файле 5 записей с данными по товарам
    item1 = Item.all[0]
    print(item1.name)

#    print(item1.calculate_amount())
#    print(item2.calculate_amount())
#    Item.pay_rate = 0.8

#    item1.apply_discount()

#    print(item1.price)
#    print(item2.price)
#    print(Item.all)

    print(Item.is_integer(5))
    print(Item.is_integer(5.0))
    print(Item.is_integer(5.5))


#    try:
#        item1 = Item("СуперКрутойСмартфон", 10000, 20)
#        print(item1.calculate_amount())
#    except NameError:
#        print("Ошибка. Длина названия товара не должна превышать 10 символов.")

#    item3 = Item("Ноутбук", 20000, 5)

#    print(item3.calculate_amount())
#    Item.pay_rate = 0.8

#    try:
#        print(item3.load_from_csv(path_csv))
#    except FileNotFoundError:
#        print(f"\nФайл {path_csv} не найден\n")

#        print(item3.price)
#        print(Item.all)
#    item3.__name = "СуперСмартфон"


if __name__ == "__main__":
    main()
