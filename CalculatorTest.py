import unittest

from Calculator import Calculator


class TestStringMethods(unittest.TestCase):
    def test_calculatorgi(self):
        self.assert_(Calculator())

    def test_buildResponse_empty_string(self):
        self.assertEquals(Calculator().buildResponse("")[0], 0)

    def test_buildResponse_single_item_string(self):
        self.assertEquals(Calculator().buildResponse("1")[0], 1)
