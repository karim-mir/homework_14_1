# Проект: Управление продуктами и категориями

## Описание

Этот проект обеспечивает функциональность для управления продуктами и категориями товаров. Он реализует создание, хранение и тестирование продуктов и их категорий.

## Структура проекта

### Модули

#### `src/product.py`

Модуль содержит класс `Product`, который представляет собой продукт. Он включает в себя атрибуты и методы для работы с продуктом.

**Класс `Product`:**

- **Атрибуты:**
  - `name`: Название продукта.
  - `description`: Описание продукта.
  - `price`: Цена продукта.
  - `quantity`: Количество товара на складе.

- **Методы:**
  - `__init__(self, name, description, price, quantity)`: Метод инициализации объекта продукта.

#### `src/category.py`

Модуль содержит класс `Category`, представляющий категорию товаров. Он включает в себя методы для работы с продуктами в категории.

**Класс `Category`:**

- **Атрибуты:**
  - `name`: Название категории.
  - `description`: Описание категории.
  - `products`: Список продуктов в категории.

- **Методы:**
  - `__init__(self, name, description, products)`: Метод инициализации объекта категории.
  - `category_count`: Возвращает общее количество категорий (в данном случае с одним объектом).
  - `quantity_products`: Возвращает общее количество продуктов в категории.

#### `src/utils.py`

Модуль содержит вспомогательные функции для работы с файлами формата JSON и создания объектов из данных.

**Функции:**

- `read_json(path: str) -> dict`: Читает данные из JSON-файла и возвращает их в виде словаря.
  - **Параметры:**
    - `path`: Путь к файлу JSON.
  - **Возвращает:**
    - Словарь данных.

- `create_objects_from_json(data: list) -> list`: Создаёт объекты категорий и продуктов на основе данных из JSON.
  - **Параметры:**
    - `data`: Список словарей, представляющих категории и их продукты.
  - **Возвращает:**
    - Список объектов `Category`.

### Тесты

#### `tests/test_product.py`

Модуль содержит тесты для проверки функциональности класса `Product`.

**Функция `test_product_init`:**
- Проверяет корректность создания объекта `Product` с предопределёнными атрибутами.

#### `tests/test_category.py`

Модуль содержит тесты для проверки функциональности класса `Category`.

**Функция `test_category`:**
- Проверяет корректность создания объекта `Category`, включая имя, описание, список продуктов и количество.

#### `tests/conftest.py`

Модуль содержит фикстуры для настройки объектов `Product` и `Category` перед выполнением тестов.

**Фикстуры:**
- `product()`: Возвращает объект `Product` с заданными параметрами.
- `category()`: Возвращает объект `Category` с предопределёнными продуктами.

## Установка

Чтобы установить проект, выполните:
```commandline
git clone 
cd <папка проекта>
```
Не забудьте установить необходимые зависимости:
```commandline
pip install -r requirements.txt
```