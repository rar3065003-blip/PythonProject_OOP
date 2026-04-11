from black import Any
from src.print_mixin import PrintMixin
from src.product import Product


class Category(PrintMixin):
    """Родительский класс"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product], should_print=False) -> None:
        self.name = name
        self.description = description
        self.__products = products
        self.should_print=should_print
        Category.category_count += 1
        Category.product_count += len(products)
        super().__init__(should_print=should_print)

    def __str__(self) -> str:
        """Оптимизирую возврат строкового отображения товаров"""
        product_summ = 0
        for product in self.__products:
            product_summ += product.quantity
        return f"{self.name}, количество продуктов: {product_summ} шт."

    def add_product(self, product: Product | Any) -> None:
        """Добавляем новый продукт"""
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError

    @property
    def products(self) -> str:
        """Возвращает форматированную строку с информацией о продуктах"""
        products_list = ""
        for product in self.__products:
            products_list += f"{str(product)}\n"
        return products_list

    @products.setter
    def products(self, new_products: list[Product]) -> None:
        """Добавляет новые продукты в категорию и обновляет счётчик"""
        for product in new_products:
            self.__products.append(product)
            Category.product_count += 1


    def middle_price_all_product(self):
        """Возвращает средний ценник всех товаров"""
        try:
            return sum([product.price for product in self.__products]) / len(self.__products)
        except ZeroDivisionError:
            return 0



