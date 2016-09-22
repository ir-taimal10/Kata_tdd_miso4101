import unittest

from Calculator import Calculator


class TestStringMethods(unittest.TestCase):
    EMPTY = ""
    SINGLE_ITEM = "5"
    TWO_ITEMS = "1,2"
    MULTIPLE_ITEMS = "1,2,3,4,5,6,7,8,9,0"

    def test_calculatorgi(self):
        self.assert_(Calculator())

    def test_buildResponse_size_empty_string(self):
        self.assertEquals(Calculator().buildResponse(self.EMPTY)[0], 0)

    def test_buildResponse_size_single_item_string(self):
        self.assertEquals(Calculator().buildResponse(self.SINGLE_ITEM)[0], 1)

    def test_buildResponse_size_two_item_string(self):
        self.assertEquals(Calculator().buildResponse(self.TWO_ITEMS)[0], 2)

    def test_buildResponse_size_multiple_item_string(self):
        self.assertEquals(Calculator().buildResponse(self.MULTIPLE_ITEMS)[0], 10)

    def test_buildResponse_minimum_empty_string(self):
        self.assertEquals(Calculator().buildResponse(self.EMPTY)[1], None)

    def test_buildResponse_minimum_single_item_string(self):
        self.assertEquals(Calculator().buildResponse(self.SINGLE_ITEM)[1], 5)

    def test_buildResponse_minimum_two_item_string(self):
        self.assertEquals(Calculator().buildResponse(self.TWO_ITEMS)[1], 1)

    def test_buildResponse_minimum_multiple_item_string(self):
        self.assertEquals(Calculator().buildResponse(self.MULTIPLE_ITEMS)[1], 0)

    def test_buildResponse_maximum_empty_string(self):
        self.assertEquals(Calculator().buildResponse(self.EMPTY)[2], None)

    def test_buildResponse_maximum_single_item_string(self):
        self.assertEquals(Calculator().buildResponse(self.SINGLE_ITEM)[2], 5)

    def test_buildResponse_maximum_two_item_string(self):
        self.assertEquals(Calculator().buildResponse(self.TWO_ITEMS)[2], 2)

    def test_buildResponse_maximum_multiple_item_string(self):
        self.assertEquals(Calculator().buildResponse(self.MULTIPLE_ITEMS)[2], 9)

    def test_buildResponse_average_empty_string(self):
        self.assertEquals(Calculator().buildResponse(self.EMPTY)[3], None)

    def test_buildResponse_average_single_item_string(self):
        self.assertEquals(Calculator().buildResponse(self.SINGLE_ITEM)[3], 5)

    def test_buildResponse_average_two_item_string(self):
        self.assertEquals(Calculator().buildResponse(self.TWO_ITEMS)[3], 1.5)
