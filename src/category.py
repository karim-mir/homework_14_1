from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        """Добавляет продукт в категорию."""
        if isinstance(
            product, Product
        ):  # Проверяем, что переданный объект является Product
            self.__products.append(product)  # Добавление продукта в список
            Category.product_count += 1
        else:
            raise ValueError("Переданный объект не является продуктом.")

    @property
    def products(self) -> list:
        """Геттер для возврата списка продуктов в формате списка словарей."""
        return [
            {
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "quantity": product.quantity,
            }
            for product in self.__products
        ]


if __name__ == "__main__":
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)  # Это теперь словарей.

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)

    print(category1.products)  # Это теперь список словарей.

    print(f"Общее количество продуктов в категории: {Category.product_count}")
