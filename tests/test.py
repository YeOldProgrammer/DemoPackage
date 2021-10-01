import pytest
from DemoPackage.demo_logic import DemoPackage


def test_str():
    str_val = 'hello world'
    demo_obj = DemoPackage(str_val=str_val)
    assert demo_obj.str_val == str_val


def test_int():
    int_val = 9
    demo_obj = DemoPackage(int_val=int_val)
    assert demo_obj.int_val == int_val


def test_execute():
    str_val = 'hello world'
    int_val = 9
    demo_obj = DemoPackage(str_val=str_val, int_val=int_val)
    demo_obj.execute()
