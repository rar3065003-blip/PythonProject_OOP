from abc import ABC, abstractmethod

from src.product import Product


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, product_data: dict, product_list: list[Product]) -> Product:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        pass

    @abstractmethod
    def check_change_price(self, new_price: float) -> float | None:
        pass

    @abstractmethod
    def __add__(self, other: Product) -> float:
        pass
