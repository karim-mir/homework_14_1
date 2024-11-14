def test_product_init(product):
    """Тест для проверки корректности создания объекта продукта.

    :param product: Объект продукта, переданный в тест через фикстуру.
    """

    # Проверка имени продукта
    assert product.name == "Iphone 15"

    # Проверка описания продукта
    assert product.description == "512GB, Gray space"

    # Проверка цены продукта
    assert product.price == 210000.0

    # Проверка количества продукта
    assert product.quantity == 8
