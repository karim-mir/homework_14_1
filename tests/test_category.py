import unittest
from src.product import Product
from src.category import Category


class TestCategory(unittest.TestCase):
    def setUp(self):
        """Настройка тестов - создание продуктов и категории."""
        self.product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        self.product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        self.product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        self.category = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [self.product1, self.product2, self.product3]
        )

    def test_initialization(self):
        """Тест инициализации класса Category."""
        self.assertEqual(self.category.name, "Смартфоны")
        self.assertEqual(self.category.description, "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни")
        self.assertEqual(len(self.category.products.splitlines()), 3)  # Три продукта должны быть в строковом представлении
        self.assertEqual(Category.category_count, 1)  # Должна быть 1 категория
        self.assertEqual(Category.product_count, 3)  # Должно быть 3 продукта

    def test_add_product(self):
        """Тест добавления продукта в категорию."""
        new_product = Product("Google Pixel 6", "128GB, Черный", 59999.0, 10)
        self.category.add_product(new_product)
        self.assertEqual(Category.product_count, 4)  # После добавления должен быть 4 продукта
        self.assertIn(new_product, self.category._Category__products)  # Проверяем, что продукт добавлен в скрытый список

    def test_add_invalid_product(self):
        """Тест добавления некорректного продукта - должен вызывать исключение."""
        with self.assertRaises(ValueError):
            self.category.add_product("Не продукт")

    def test_total_value(self):
        """Тест расчета общей стоимости продуктов в категории."""
        expected_total = (self.product1.price * self.product1.quantity +
                          self.product2.price * self.product2.quantity +
                          self.product3.price * self.product3.quantity)
        self.assertAlmostEqual(self.category.total_value(), expected_total)

    def test_products_string(self):
        """Тест для проверки корректности строки, возвращаемой методами products."""
        expected_products = (
            'Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n'
            'Iphone 15, 210000.0 руб. Остаток: 8 шт.\n'
            'Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n'
        )
        self.assertEqual(self.category.products, expected_products)

    def tearDown(self):
        """Очистка после тестов."""
        Category.category_count -= 1
        Category.product_count -= len(self.category._Category__products)


if __name__ == '__main__':
    unittest.main()
