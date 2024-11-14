class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)
