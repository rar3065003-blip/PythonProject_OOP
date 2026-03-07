from itertools import product
from typing import AnyStr


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, product_data:dict, product_list:list) -> 'Product':
        for existing_product in product_list:
            if existing_product.name == product_data['name']:
                if product_data['price'] > existing_product.__price:
                    existing_product.__price = product_data['price']
                existing_product.quantity += product_data['quantity']
                return existing_product

        return cls(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                quantity=product_data['quantity']
                )

    @property
    def price(self)->float:
        """Принимаем цену из привата"""
        return float(self.__price)

    @price.setter
    def price(self, value):
        """Возвращает строку с ценой или сообщением об ошибке"""
        if value <= 0:
            print("Цена не должна быть нулевой или отрицательной")
            return
        self.__price = value