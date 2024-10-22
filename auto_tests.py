import unittest

from main import my_sum_func


class MyTestCase(unittest.TestCase):
    def test_my_sum(self):
        self.assertEqual(my_sum_func(1, 1), 2)


if __name__ == '__main__':
    unittest.main()
