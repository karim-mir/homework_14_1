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


def test_product_set_price(product):
    """Тест для проверки установки корректной цены."""

    # Установка новой корректной цены
    product.price = 250000.0
    assert product.price == 250000.0


def test_product_set_negative_price(product):
    """Тест для проверки установки некорректной (отрицательной) цены."""

    # Попытка установить отрицательную цену
    try:
        product.price = -100
    except ValueError as e:
        assert str(e) == "Цена не должна быть нулевая или отрицательная"


def test_product_set_zero_price(product):
    """Тест для проверки установки некорректной (нулевой) цены."""

    # Попытка установить нулевую цену
    try:
        product.price = 0
    except ValueError as e:
        assert str(e) == "Цена не должна быть нулевая или отрицательная"
