import unittest
from src.product import Product
from unittest.mock import patch

class TestProduct(unittest.TestCase):

    def setUp(self):
        """Создание тестовых данных для каждого теста."""
        self.product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        self.product2 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)

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

    @patch('builtins.print')
    def test_set_price_invalid(self, mock_print):
        """Тест на установку некорректной (отрицательной) цены."""
        self.product1.price = -100.0  # Это должно вывести сообщение об ошибке
        mock_print.assert_called_with("Цена не должна быть нулевой или отрицательной")
        self.assertEqual(self.product1.price, 210000.0)  # Проверяем, цена не изменилась

    @patch('builtins.print')
    def test_set_price_zero(self, mock_print):
        """Тестируем, что нельзя установить нулевую цену."""
        self.product1.price = 0
        mock_print.assert_called_with("Цена не должна быть нулевой или отрицательной")
        self.assertEqual(self.product1.price, 210000.0)  # предыдущая цена должна остаться

    def test_addition_of_products(self):
        """Тест сложения двух продуктов (только цены)."""
        total_price = self.product1 + self.product2
        self.assertEqual(total_price, 210000.0 * 8 + 180000.0 * 5)

    def test_addition_invalid_type(self):
        """Проверка добавления продукта к объекту другого типа (должно вызвать исключение)."""
        with self.assertRaises(ValueError):
            result = self.product1 + "Не продукт"  # Это не допустимый объект

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

if __name__ == "__main__":
    unittest.main()
