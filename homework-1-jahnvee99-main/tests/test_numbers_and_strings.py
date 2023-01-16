import pytest

from mypkg.my_answers import numbers_and_strings

x, y, z, length, m, n = numbers_and_strings()


def test_power():
    assert(x == 1024)


def test_string():
    assert(y == "Stevens")


def test_repeat():
    assert(len(z) == 7 * len("Stevens"))


def test_len():
    assert(length == 49)


def test_concat():
    assert(m == "Stevens is Great")


def test_replace():
    assert(n == "Stevens is Good")


