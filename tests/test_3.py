from tasks import task_3
import unittest


class Test(unittest.TestCase):

    def test_max_prime_div_6(self):
        self.assertEqual(task_3.get_max_prime_divider(6), 3)

    def test_max_prime_div_10(self):
        self.assertEqual(task_3.get_max_prime_divider(10), 5)

    def test_max_prime_div_13195(self):
        self.assertEqual(task_3.get_max_prime_divider(13195), 29)

    def test_max_prime_div_600851475143(self):
        self.assertEqual(task_3.get_max_prime_divider(600851475143), 6857)


if __name__ == '__main__':
    unittest.main()
