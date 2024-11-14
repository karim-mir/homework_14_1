def test_category(category):
    """Тест для проверки корректности создания объекта категории.

    :param category: Объект категории, переданный в тест через фикстуру.
    """
    # Проверка имени категории
    assert category.name == "Смартфоны"

    # Проверка описания категории
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )

    # Проверка списка продуктов в категории
    assert category.products == [
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

    # Проверка общего количества категорий
    assert category.category_count == 1

    # Проверка общего количества продуктов в категориях
    assert category.product_count == 3
