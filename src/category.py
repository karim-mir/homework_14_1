import json
import os

from src.product import LawnGrass, Product, Smartphone


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

    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5,
        95.5,
        "S23 Ultra",
        256,
        "Серый",
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11",
        "1024GB, Синий",
        31000.0,
        14,
        90.3,
        "Note 11",
        1024,
        "Синий",
    )
    print(smartphone1.name)
    print(smartphone1.description)
    print(smartphone1.price)
    print(smartphone1.quantity)
    print(smartphone1.efficiency)
    print(smartphone1.model)
    print(smartphone1.memory)
    print(smartphone1.color)
    print(smartphone2.name)
    print(smartphone2.description)
    print(smartphone2.price)
    print(smartphone2.quantity)
    print(smartphone2.efficiency)
    print(smartphone2.model)
    print(smartphone2.memory)
    print(smartphone2.color)
    print(smartphone3.name)
    print(smartphone3.description)
    print(smartphone3.price)
    print(smartphone3.quantity)
    print(smartphone3.efficiency)
    print(smartphone3.model)
    print(smartphone3.memory)
    print(smartphone3.color)
    grass1 = LawnGrass(
        "Газонная трава",
        "Элитная трава для газона",
        500.0,
        20,
        "Россия",
        "7 дней",
        "Зеленый",
    )
    grass2 = LawnGrass(
        "Газонная трава 2",
        "Выносливая трава",
        450.0,
        15,
        "США",
        "5 дней",
        "Темно-зеленый",
    )
    print(grass1.name)
    print(grass1.description)
    print(grass1.price)
    print(grass1.quantity)
    print(grass1.country)
    print(grass1.germination_period)
    print(grass1.color)
    print(grass2.name)
    print(grass2.description)
    print(grass2.price)
    print(grass2.quantity)
    print(grass2.country)
    print(grass2.germination_period)
    print(grass2.color)
    smartphone_sum = smartphone1 + smartphone2
    print(smartphone_sum)
    grass_sum = grass1 + grass2
    print(grass_sum)

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError:
        print("Возникла ошибка TypeError при попытке сложения")
    else:
        print("Не возникла ошибка TypeError при попытке сложения")

    category_smartphones = Category(
        "Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2]
    )
    category_grass = Category(
        "Газонная трава", "Различные виды газонной травы", [grass1, grass2]
    )
    category_smartphones.add_product(smartphone3)
    print(category_smartphones.products)
    print(Category.product_count)

    try:
        category_smartphones.add_product("Not a product")
    except ValueError:
        print("Возникла ошибка ValueError при добавлении не продукта")
    else:
        print("Не возникла ошибка ValueError при добавлении не продукта")

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
