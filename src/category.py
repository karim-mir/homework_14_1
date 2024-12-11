import json
import os

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
        self.__products = products if products is not None else []
        if not self.__products:  # Вызывается только, если __products пуст
            self.load_products()
        Category.category_count += 1

    def load_products(self):
        """Загружает продукты из data.json и добавляет их в категорию."""
        try:
            with open(
                os.path.join("..", "data", "data.json"), "r", encoding="utf-8"
            ) as f:
                categories_data = json.load(f)
                for category in categories_data:
                    if category["name"] == self.name:
                        for product_data in category["products"]:
                            product = Product(
                                product_data["name"],
                                product_data["description"],
                                product_data["price"],
                                product_data["quantity"],
                            )
                            self.__products.append(product)
                        break  # Прекращаем, если нашли нужную категорию
        except FileNotFoundError:
            print("Файл data.json не найден.")
        except json.JSONDecodeError:
            print("Ошибка чтения файла data.json.")

    def __str__(self):
        """Выводит название категории и общее количество всех товаров."""
        total_quantity = sum(
            product.quantity for product in self.__products
        )  # Суммируем количество всех товаров
        return f"{self.name}, количество продуктов: {total_quantity} шт."

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
    def products(self):
        """Геттер для возврата списка продуктов в формате строки."""
        return "\n".join(str(product) for product in self.__products)


if __name__ == "__main__":
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    )

    print(str(category1))  # Вывод названия категории и количества продуктов
    print(category1.products)  # Вывод всех продуктов категории
