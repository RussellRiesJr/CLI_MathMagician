from mathmagician import *
import unittest

class TestMathMagician(unittest.TestCase):

    @classmethod
    def setUpClass(self):
      self.mathThing = MathTest()

    def test_fibonacci(self):
      fib = self.mathThing.generate_fibonacci(6)
      self.assertEqual([0, 1, 1, 2, 3, 5], fib)

    def test_integers(self):
      integers = self.mathThing.generate_intergers(6)
      self.assertEqual([0, 1, 2, 3, 4, 5], integers)

    def test_primes(self):
      primes = self.mathThing.generate_primes(6)
      self.assertEqual([2, 3, 5, 7, 11, 13], primes)


if __name__ == '__main__':
    unittest.main()
