import json
import os
from src.category import Category
from src.product import Product


def read_json(path: str) -> dict:
    """
    Читает JSON файл и возвращает его содержимое в виде словаря.

    :param path: Путь к файлу JSON.
    :return: Данные из JSON файла в виде словаря.
    """
    # Получаем полный путь к файлу
    full_path = os.path.abspath(path)

    # Открываем и читаем файл, декодируем JSON данные
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)

    return data


def create_objects_from_json(data: list) -> list:
    """
    Создаёт объекты категорий и продуктов на основе предоставленных данных.

    :param data: Список словарей, представляющих категории и их продукты.
    :return: Список объектов Category.
    """
    categories = []  # Список для хранения объектов категорий

    for category_data in data:
        # Создаем объект категории
        category = Category(
            name=category_data["name"], description=category_data["description"]
        )

        # Создаем список продуктов для текущей категории
        products = [
            Product(**product_data) for product_data in category_data["products"]
        ]
        category.products = products  # Сохраняем продукты в категории

        # Добавляем категорию в список
        categories.append(category)

    return categories


if __name__ == "__main__":
    # Читаем сырые данные из JSON файла
    raw_data = read_json("../data/data.json")

    # Создаем объекты категорий и продуктов из считанных данных
    categories_data = create_objects_from_json(raw_data)

    # Пример вывода информации о первой категории и её продуктах
    print(categories_data[0].name)  # Имя первой категории
    for product in categories_data[0].products:  # Продукты первой категории
        print(
            f"  Продукт: {product.name}, Цена: {product.price}, Количество: {product.quantity}"
        )
