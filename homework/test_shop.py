"""
Протестируйте классы из модуля homework/models.py
"""
import pytest
from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def product2():
    return Product("pen", 0, "This is a pen", 0)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(15) is True
        assert product.check_quantity(1500) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(1) == 1001

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            assert product.buy(1111)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_products(self, cart, product):
        cart.add_product(product, 22)
        assert cart.products[product] == 22

        cart.add_product(product, 8)
        assert cart.products[product] == 30

    def test_delete_product(self, cart, product):
        cart.add_product(product, 5)
        cart.remove_product(product, 3)
        assert cart.products[product] == 2

        cart.remove_product(product, 1)
        assert cart.products[product] == 1

    def test_delete_product_more_than_available(self, cart, product):
        cart.add_product(product, 2)
        cart.remove_product(product, 2)
        with pytest.raises(KeyError):
            assert cart.products[product]

    def test_clear(self, cart, product):
        cart.add_product(product, 5)
        assert cart.products[product] == 5

        cart.clear()
        assert product not in cart.products

        with pytest.raises(KeyError):
            assert cart.products[product]

    def test_buy(self, cart, product):
        cart.add_product(product, 11)
        cart.buy()
        assert product.quantity == 1011

    def test_buy_more(self, cart, product):
        cart.add_product(product, 1111)
        with pytest.raises(ValueError):
            cart.buy()

    def test_balance_empty_cart(self, cart, product2):
        assert cart.get_total_price() == 0

    def test_get_balance(self, cart, product):
        assert cart.get_total_price() == 0
        cart.add_product(product, 5)
        assert cart.get_total_price() == 500
