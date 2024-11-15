from src.product import Product


def test_category(category):
    """Тест для проверки корректности создания объекта категории.

    :param category: Объект категории, переданный в тест через фикстуру.
    """
    # Проверка имени категории
    assert category.name == "Смартфоны"

    # Проверка описания категории
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )

    # Проверка списка продуктов в категории
    expected_products = [
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
    ]

    # Используем category.product_list для получения списка продуктов
    assert category.products == expected_products  # Сравниваем с ожидаемым списком

    # Проверка общего количества категорий
    assert category.category_count == 1

    # Проверка общего количества продуктов в категориях
    assert category.product_count == 3

    # Создание нового продукта и добавление его в категорию
    new_product = Product("Google Pixel 6", "128GB, Черный", 59999.0, 10)
    category.add_product(new_product)

    # Проверяем, что новый продукт добавлен
    assert category.product_count == 4  # Обновляемое количество продуктов
