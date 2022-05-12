import unittest

from arithmetic_operations import four, times, five, one, plus, eight, seven, minus, three, nine, divided_by


class MyTestCase(unittest.TestCase):
    value_times = 20
    value_plus = 9
    value_minus = 4
    value_divided = 3
    message = "First value and second value are not equal !"

    def test_times(self):
        result_times = four(times(five()))
        self.assertEqual(result_times, self.value_times, self.message)

    def test_plus(self):
        result_plus = one(plus(eight()))
        self.assertEqual(result_plus, self.value_plus, self.message)

    def test_minus(self):
        result_minus = seven(minus(three()))
        self.assertEqual(result_minus, self.value_minus, self.message)

    def test_divided(self):
        result_divided = nine(divided_by(three()))
        self.assertEqual(result_divided, self.value_divided, self.message)


if __name__ == '__main__':
    unittest.main()
