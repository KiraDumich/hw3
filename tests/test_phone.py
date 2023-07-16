from src.phone import Phone
from src.item import Item
import pytest


# test 1
def test_value_error():
    item1 = Phone('Iphone', 34000, 5, 2)
    assert item1.name == 'Iphone'


# test 2
def test_repr():
    item1 = Phone('Iphone', 34000, 5, 2)
    assert repr(item1) == "Phone('Iphone', 34000, 5, 2)"


# test 3
def test_add():
    item1 = Item('Huawei', 23000, 15)
    phone1 = Phone('Iphone', 35000, 14, 2)
    assert item1 + phone1 == 29

