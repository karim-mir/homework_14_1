import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    """Создает и возвращает экземпляр продукта 'Iphone 15' для использования в тестах.

    :return: Объект Product с предопределенными атрибутами.
    """
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category():
    """Создает и возвращает экземпляр категории 'Смартфоны' с предопределенными продуктами для использования в тестах.

    :return: Объект Category с предопределенными атрибутами и списком продуктов.
    """
    # Создаем экземпляры продуктов
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создаем и возвращаем категорию с продуктами
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных "
        "функций для удобства жизни",
        products=[product1, product2, product3],  # Передаем объекты Product
    )
