import unittest
from unittest.mock import patch

from src.product import LawnGrass, Product, Smartphone


class TestProduct(unittest.TestCase):

    def setUp(self):
        """Создание тестовых данных для каждого теста."""
        self.product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        self.product2 = Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5
        )

    def test_initialization(self):
        """Тест на правильность инициализации продукта."""
        self.assertEqual(self.product1.name, "Iphone 15")
        self.assertEqual(self.product1.description, "512GB, Gray space")
        self.assertEqual(self.product1.price, 210000.0)
        self.assertEqual(self.product1.quantity, 8)

    def test_set_price_valid(self):
        """Тест на корректную установку цены продукта."""
        self.product1.price = 250000.0
        self.assertEqual(self.product1.price, 250000.0)

    @patch("builtins.print")
    def test_set_price_invalid(self, mock_print):
        """Тест на установку некорректной (отрицательной) цены."""
        self.product1.price = -100.0  # Это должно вывести сообщение об ошибке
        mock_print.assert_called_with("Цена не должна быть нулевой или отрицательной")
        self.assertEqual(self.product1.price, 210000.0)  # Проверяем, цена не изменилась

    @patch("builtins.print")
    def test_set_price_zero(self, mock_print):
        """Тестируем, что нельзя установить нулевую цену."""
        self.product1.price = 0
        mock_print.assert_called_with("Цена не должна быть нулевой или отрицательной")
        self.assertEqual(
            self.product1.price, 210000.0
        )  # предыдущая цена должна остаться

    def test_addition_of_products(self):
        """Тест сложения двух продуктов (только цены)."""
        total_price = self.product1 + self.product2
        self.assertEqual(total_price, 210000.0 * 8 + 180000.0 * 5)

    def test_addition_invalid_type(self):
        """Проверка добавления продукта к объекту другого типа (должно вызвать исключение)."""
        with self.assertRaises(ValueError):
            self.product1 + "Не продукт"  # Это не допустимый объект

    def test_new_product_class_method(self):
        """Тест на создание нового продукта через класс-метод."""
        product_data = {
            "name": "Xiaomi Redmi Note 11",
            "description": "1024GB, Синий",
            "price": 31000.0,
            "quantity": 14,
        }
        product3 = Product.new_product(product_data)
        self.assertEqual(product3.name, "Xiaomi Redmi Note 11")
        self.assertEqual(product3.price, 31000.0)
        self.assertEqual(product3.quantity, 14)


class TestSmartphone(unittest.TestCase):
    def setUp(self):
        """Создание тестовых данных для каждого теста."""
        self.smartphone1 = Smartphone(
            "Iphone 15", "512GB, Gray space", 210000.0, 8, 15, "iPhone 15", 512, "Gray"
        )
        self.smartphone2 = Smartphone(
            "Samsung Galaxy S23 Ultra",
            "256GB, Серый цвет",
            180000.0,
            5,
            14,
            "Galaxy S23",
            256,
            "Gray",
        )

    def test_smartphone_initialization(self):
        """Тест на правильность инициализации смартфона."""
        self.assertEqual(self.smartphone1.name, "Iphone 15")
        self.assertEqual(self.smartphone1.price, 210000.0)
        self.assertEqual(self.smartphone1.memory, 512)

    def test_smartphone_addition(self):
        """Тест сложения двух смартфонов."""
        total_price = self.smartphone1 + self.smartphone2
        self.assertEqual(total_price, 210000.0 + 180000.0)

    def test_smartphone_addition_invalid_type(self):
        """Проверка добавления смартфона к объекту другого типа (должно вызвать исключение)."""
        with self.assertRaises(TypeError):
            self.smartphone1 + "Не смартфон"  # Это не допустимый объект


class TestLawnGrass(unittest.TestCase):
    def setUp(self):
        """Создание тестовых данных для каждого теста."""
        self.lawn_grass1 = LawnGrass(
            "Курганник", "Служит для газонов", 2500.0, 20, "Россия", 30, "Зеленый"
        )
        self.lawn_grass2 = LawnGrass(
            "Райграс", "Лучший газонный", 3000.0, 15, "Канада", 25, "Темно-зеленый"
        )

    def test_lawn_grass_initialization(self):
        """Тест на правильность инициализации газона."""
        self.assertEqual(self.lawn_grass1.name, "Курганник")
        self.assertEqual(self.lawn_grass1.price, 2500.0)
        self.assertEqual(self.lawn_grass1.country, "Россия")

    def test_lawn_grass_addition(self):
        """Тест сложения двух видов газонов."""
        total_price = self.lawn_grass1 + self.lawn_grass2
        self.assertEqual(total_price, 2500.0 + 3000.0)

    def test_lawn_grass_addition_invalid_type(self):
        """Проверка добавления газона к объекту другого типа (должно вызвать исключение)."""
        with self.assertRaises(TypeError):
            self.lawn_grass1 + "Не газон"  # Это не допустимый объект


class TestPrintMixin:
    def test_print_mixin(self, capsys):
        # Создаем экземпляр класса Product, что должно вызвать вывод
        Product(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
        )

        # Захватываем стандартный вывод
        message = capsys.readouterr()

        # Проверяем, что вывод в консоль соответствует ожидаемому
        assert message.out.strip() == (
            "Product, (Samsung Galaxy S23 Ultra, 256GB, "
            "Серый цвет, 200MP камера, 180000.0, 5)"
        )


class ProductInvalidQuantity(unittest.TestCase):

    def test_invalid_quantity(self):
        with self.assertRaises(ValueError) as context:
            Smartphone(
                "Iphone 15",
                "512GB, Gray space",
                210000.0,
                0,
                15,
                "iPhone 15",
                512,
                "Gray",
            )

        self.assertEqual(
            str(context.exception), "Товар с нулевым количеством не может быть добавлен"
        )


if __name__ == "__main__":
    unittest.main()
