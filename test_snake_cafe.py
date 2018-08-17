from .snake_cafe import tax, order_total,load_csv_menu
import pytest





def test_tax():
    expected = 1.01
    actual = tax(10)
    assert expected == actual
    

def test_order_total():
    expected =  11.01
    actual = 10 + tax(10)
    assert expected == actual

def test_type_of_load():
    expected = 'dict'
    actual  = type(load_csv_menu())
    assert expected == actual








