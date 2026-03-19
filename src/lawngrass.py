from src.product import Product


class LawnGrass(Product):
    """Дочерний класс принимающий родительский класс Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self) -> str:
        """Наглядное представление продукта для удобочитаемости"""
        return (
            f"{super().__str__()} Страна: {self.country},"
            f" Срок прорастания: {self.germination_period}, Цвет: {self.color}"
        )

    def __add__(self, other: "Product") -> float:
        """Складываем все товары одного типа и получаем стоимость товара типа на складе"""
        if type(self) is type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
