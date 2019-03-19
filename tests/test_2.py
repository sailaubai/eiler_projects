from tasks import task_2
import unittest


class Test(unittest.TestCase):

    def test_5(self):
        self.assertEqual(task_2.sum_fib(5), 12)

    def test_20(self):
        self.assertEqual(task_2.sum_fib(7000), 17710)

    def test_33(self):
        self.assertEqual(task_2.sum_fib(), 9227464)


if __name__ == "__main__":
    unittest.main()
