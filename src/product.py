from typing import List


class Product:

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data: dict, product_list: List["Product"]) -> "Product":
        """Принимает вход параметры товара в словаре и возвращать созданный объект класса"""
        for existing_product in product_list:
            if existing_product.name == product_data["name"]:
                if product_data["price"] > existing_product.__price:
                    existing_product.__price = product_data["price"]
                existing_product.quantity += product_data["quantity"]
            return existing_product

        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self) -> float:
        """Принимаем цену из привата"""
        return float(self.__price)

    @price.setter
    def price(self, value: float) -> None:
        """Возвращает строку с ценой или сообщением об ошибке"""
        if value <= 0:
            print("Цена не должна быть нулевой или отрицательной")
            return
        self.__price = value

    def check_change_price(self, new_price: float) -> float | None:
        """Изменение цены в случае ее понижения с согласия пользователя"""
        if self.price != new_price:
            user_confirmed = input("Вы уверены, что хотите изменить цену? (y/n):")
            if user_confirmed.lower() == "y":
                self.price = new_price
                return self.price
            elif user_confirmed.lower() == "n":
                return self.price
            return None
        else:
            return self.price
