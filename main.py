class CoffeeShop:
    def __init__(self):
        self.menu = {'Латте': 35, 'Еспресо': 40, 'Американо': 45, 'Раф': 40, }
        self.order = {}
        self.cash = 1000  # Початкова сума готівки
        self.cost_per_item = {key: value / 100 for key, value in self.menu.items()}

    def display_menu(self):
        print("Меню:")
        for item, price in self.menu.items():
            print(f"{item}: {price} грн")

    def take_order(self):
        while True:
            item = input("Введіть назву товару (або 'кінець', щоб завершити замовлення): ").capitalize()

            if item == 'Кінець':
                break

            if item not in self.menu:
                add_to_menu = input(f"Товару '{item}' немає у меню. Бажаєте продовжити?(Так/Ні): ").lower()
                if add_to_menu == 'так':
                 continue
                else:
                    break

            quantity = int(input(f"Введіть кількість '{item}': "))

            if item in self.order:
                self.order[item] += quantity
            else:
                self.order[item] = quantity

    def display_order(self):
        print("\nЗамовлення:")
        for item, quantity in self.order.items():
            price = self.menu[item]
            total_price = quantity * price
            print(f"{item} x {quantity} = {total_price} грн")

    def calculate_total(self):
        total = sum(self.menu[item] * quantity for item, quantity in self.order.items())
        print(f"\nЗагальна вартість замовлення: {total} грн")
        self.cash -= total
        print(f"Залишок готівки: {self.cash} грн")
        for item, quantity in self.order.items():
            print(f"Ціна одного '{item}': {self.cost_per_item[item]} грн")


if __name__ == "__main__":
    coffee_shop = CoffeeShop()

    coffee_shop.display_menu()
    coffee_shop.take_order()
    coffee_shop.display_order()
    coffee_shop.calculate_total()