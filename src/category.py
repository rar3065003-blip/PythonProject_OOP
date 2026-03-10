from src.product import Product


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляем новый продукт"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает форматированную строку с информацией о продуктах"""
        products_list = ""
        for product in self.__products:
            products_list += (
                f"Название продукта: {product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            )
        return products_list

    @products.setter
    def products(self, new_products: list[Product]) -> None:
        """Добавляет новые продукты в категорию и обновляет счётчик"""
        for product in new_products:
            self.__products.append(product)
            Category.product_count += 1
