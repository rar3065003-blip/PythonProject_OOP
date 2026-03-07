from itertools import product


class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


    @classmethod
    def new_product(cls, product_data:dict, product_list) -> 'Product':
        for existing_product in product_list:
            if existing_product.name == product_data['name']:
                if product_data['price'] > existing_product.price:
                    existing_product.price = product_data['price']
                existing_product.quantity += existing_product.quantity

        return cls(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                quantity=product_data['quantity']
                )
