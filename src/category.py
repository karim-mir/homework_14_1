from itertools import product

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

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."

    def add_product(self, product: Product):
        """Добавляет продукт в категорию."""
        if isinstance(
            product, Product
        ):  # Проверяем, что переданный объект является Product
            self.__products.append(product)  # Добавление продукта в список
            Category.product_count += 1
        else:
            raise ValueError("Переданный объект не является продуктом.")

    def total_value(self) -> float:
        """Вычисляет общую стоимость всех товаров в категории."""
        total = 0.0
        for product in self.__products:
            total += product.price * product.quantity
        return total

    @property
    def products(self) -> str:
        """Геттер для возврата списка продуктов в формате строки."""
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
