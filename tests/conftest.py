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
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для "
        "удобства жизни",
        products=[
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5,
            },
            {
                "name": "Iphone 15",
                "description": "512GB, Gray space",
                "price": 210000.0,
                "quantity": 8,
            },
            {
                "name": "Xiaomi Redmi Note 11",
                "description": "1024GB, Синий",
                "price": 31000.0,
                "quantity": 14,
            },
        ],
    )
