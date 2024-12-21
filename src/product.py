from abc import ABC, abstractmethod


class PrintMixin:
    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}, ({self.name}, {self.description}, {self.price}, {self.quantity})"


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class Product(BaseProduct, PrintMixin):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price  # Вызов сеттера для установки цены
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Определяем, как складываются два продукта."""
        if isinstance(other, Product):
            return (self.price * self.quantity) + (
                other.price * other.quantity
            )  # Сложение цен двух продуктов
        raise ValueError("Можно складывать только с экземпляром Product.")

    @classmethod
    def new_product(cls, product_data):
        """Создает новый продукт из словаря и возвращает его экземпляр."""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self):
        """Геттер для получения текущей цены."""
        return self.__price

    @price.setter
    def price(self, value):
        """Сеттер для установки цены с проверкой на положительность."""
        if value <= 0:
            print("Цена не должна быть нулевой или отрицательной")
        else:
            self.__price = (
                value  # Устанавливаем новое значение цены, если оно корректно
            )


class Smartphone(Product, BaseProduct, PrintMixin):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other):
        if type(other) is Smartphone:
            return self.price + other.price
        raise TypeError


class LawnGrass(Product, BaseProduct, PrintMixin):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other):
        if type(other) is LawnGrass:
            return self.price + other.price
        raise TypeError


if __name__ == "__main__":
    # Пример использования класса-метода new_product
    product_data = {
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8,
    }

    product = Product.new_product(product_data)

    print(product.name)
    print(product.description)
    print(product.price)
    print(product.quantity)

    # Пробуем установить некорректную цену
    product.price = -100  # Должно вывести сообщение об ошибке
    print(product.price)  # Цену не установим, выводим прежнюю цену

    # Пробуем установить корректную цену
    product.price = 250000.0  # Правильное значение
    print(product.price)  # Выводим новую цену
