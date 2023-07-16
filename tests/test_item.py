import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def test_calculate_total_price():
    sofia = Item('Sofia', 3400, 5)
    assert sofia.calculate_total_price() == 17000


def test_apply():
    sofia = Item('Sofia', 3400, 5)
    Item.pay_rate = 0.2
    sofia.apply_discount()
    assert Item.price == 680


def test_string_to_number():
    assert Item.string_to_number('6') == 6


def test_name():
    test = Item('Telephones', 89, 8)
    assert test.name == 'Telephones'


def test_name_2():
    test2 = Item('Laptop', 78, 9)
    test2.name = 'Computer'
    assert test2.name == 'Computer'


def test_repr():
    test_1 = Item('Iphone', 34500, 5)
    assert repr(test_1) == "Item('Iphone', 34500, 5)"


def test_str():
    test_1 = Item('Iphone', 34500, 5)
    assert str(test_1) == 'Iphone'


def test_add():
    item1 = Item('Huawei', 23000, 15)
    phone1 = Phone('Iphone', 35000, 14, 2)
    assert item1 + phone1 == 29