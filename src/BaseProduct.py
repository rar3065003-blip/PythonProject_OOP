from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @abstractmethod
    def new_product(self, product_data: dict, product_list):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def check_change_price(self, new_price):
        pass

    @abstractmethod
    def __add__(self, other):
        pass



