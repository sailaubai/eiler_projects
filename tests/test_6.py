import unittest
from tasks import task_6


class Test(unittest.TestCase):

    def test_10(self):
        self.assertEqual(task_6.difference_arithmetic_progress(10), 2640)

    def test_100(self):
        """
        25502500 - 338350 = 25164150
        """
        self.assertEqual(task_6.difference_arithmetic_progress(100), 25164150)


if __name__ == '__main__':
    unittest.main()
