import unittest

from Calculator import Calculator


class TestStringMethods(unittest.TestCase):
    def test_calculatorgi(self):
        self.assert_(Calculator())

    def test_buildResponse_size_empty_string(self):
        self.assertEquals(Calculator().buildResponse("")[0], 0)

    def test_buildResponse_size_single_item_string(self):
        self.assertEquals(Calculator().buildResponse("1")[0], 1)

    def test_buildResponse_size_two_item_string(self):
        self.assertEquals(Calculator().buildResponse("1,2")[0], 2)

    def test_buildResponse_size_multiple_item_string(self):
        self.assertEquals(Calculator().buildResponse("1,2,3,4,5,6,7,8,9,0")[0], 10)

    def test_buildResponse_minimum_empty_string(self):
        self.assertEquals(Calculator().buildResponse("")[1], None)
