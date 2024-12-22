import pytest

from src.category import Category
from src.product import Product


def test_category_creation(category):
    """Проверяет создание категории с предопределенными продуктами."""
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category._Category__products) == 3  # Проверяем количество продуктов


def test_str_method(category):
    """Проверяет метод __str__ класса Category."""
    expected_str = "Смартфоны, количество продуктов: 27 шт."  # 5 + 8 + 14 = 27
    assert str(category) == expected_str


def test_add_product(category):
    """Проверяет добавление продукта в категорию."""
    new_product = Product("Google Pixel 7", "128GB, Черный", 60000.0, 10)
    category.add_product(new_product)

    # Проверяем, что добавленный продукт теперь в категории
    assert len(category._Category__products) == 4  # 3 существующих + 1 новый
    assert category._Category__products[-1].name == "Google Pixel 7"


def test_add_invalid_product(category):
    """Проверяет добавление некорректного продукта."""
    with pytest.raises(ValueError, match="Переданный объект не является продуктом."):
        category.add_product("not a product")


def test_products_property(category):
    """Проверяет свойство products, возвращающее строку с продуктами."""
    expected_products_str = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт."
    )
    assert category.products == expected_products_str


def test_middle_price_with_products():
    """Проверяет среднюю цену всех продуктов в категории"""
    category = Category("Electronics", "Various electronic devices")

    # Добавляем продукты в категорию
    product1 = Product("Smartphone", "Latest model", 1000.0, 2)  # 2000.0
    product2 = Product("Laptop", "Gaming laptop", 2000.0, 3)  # 6000.0
    category.add_product(product1)
    category.add_product(product2)

    # Ожидаемая средняя цена
    expected_middle_price = round((1000.0 * 2 + 2000.0 * 3) / (2 + 3), 2)

    # Получаем среднюю цену
    round_middle_price = category.middle_price()

    # Проверяем, что средняя цена соответствует ожидаемой
    assert round_middle_price == expected_middle_price


def test_invalid_middle_price_empty_category():
    """Проверяет работу функции при пустом списке продуктов в категории"""
    category = Category("Empty Category", "No products here")

    # Получаем среднюю цену
    round_middle_price = category.middle_price()

    # Проверяем, что средняя цена равна 0
    assert round_middle_price == 0


if __name__ == "__main__":
    pytest.main()
