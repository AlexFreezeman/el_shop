from utils.item import Item


def main():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    print(item1.calculate_amount())
    print(item2.calculate_amount())
    Item.pay_rate = 0.8

    item1.apply_discount()

    print(item1.price)
    print(item2.price)
    print(Item.all)



if __name__ == "__main__":
    main()