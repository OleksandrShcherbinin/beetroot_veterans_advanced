import unittest
from fractions import Fraction


assert sum([1, 2, 3]) == 6, 'Should be 6'


def test_sum():
    assert sum([1, 2, 3]) == 6, 'Should be 6'


def test_sum_tuple():
    assert sum((1, 2, 3)) == 6, 'Should be 6'


def my_sum(*args):
    total = 0
    for number in args:
        total += number

    return total


class MySumTestCase(unittest.TestCase):

    def test_integer_success(self):
        data = [5, 6, 3]  # Arrange

        result = my_sum(*data)  # Act

        self.assertEqual(result, 14)  # Assert

    def test_integer_tuple_success(self):
        data = (5, 6, 3)  # Arrange

        result = my_sum(*data)  # Act

        self.assertEqual(result, 14)  # Assert

    def test_float_success(self):
        data = (0.5, 0.5, 0.5)  # Arrange

        result = my_sum(*data)  # Act

        self.assertEqual(result, 1.5)  # Assert

    def test_weird_float_success(self):
        data = (0.3, 0.3, 0.3)  # Arrange

        result = my_sum(*data)  # Act

        self.assertAlmostEqual(result, 0.9, 2)  # Assert

    def test_fraction_success(self):
        data = (Fraction(1, 4), Fraction(1, 4), Fraction(1, 2))  # Arrange

        result = my_sum(*data)  # Act

        self.assertEqual(result, 1)  # Assert

    def test_wrong_type(self):
        data = ['banana', 'orange', 'apple']

        with self.assertRaises(TypeError):
            my_sum(*data)


# if __name__ == '__main__':
#     unittest.main()
