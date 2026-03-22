from src.product import Product


class Smartphone(Product):
    """Дочерний класс принимающий родительский класс Product"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        """Наглядное представление продукта для удобочитаемости"""
        return f"{super().__str__()} Модель: {self.model}," f" Память: {self.memory}GB, Цвет: {self.color}"

    def __add__(self, other: "Product") -> float:
        """Складываем все товары одного типа и получаем стоимость товара типа на складе"""
        if type(self) is type(other):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError
