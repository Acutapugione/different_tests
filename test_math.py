from typing import Literal
import unittest
from unittest import TestCase
from my_math import square, square_root, root

class MyTest(TestCase):
    def test_square(self):#For 1 Unit
        self.assertAlmostEqual(first=square(-2.5), second=6, delta=0.25)
        self.assertEqual(square(2), 4)

    def test_square_root(self):
        self.assertEqual(square_root(100), 10)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(1), 1)
        self.assertAlmostEqual(square_root(-100), 6e-16+10j, delta=0.25)
        self.assertAlmostEqual(square_root(-25), 3e-16 + 5j, delta=0.25)
        
        self.assertAlmostEqual(square_root(11), 3, delta=0.4)
        self.assertAlmostEqual(square_root(10), 3, delta=0.4)
        
    def test_root(self):
        self.assertEqual(root(100, 2), 10)
        self.assertIsInstance(root(100, 2), float)
        self.assertEqual(root(-100, -1), -0.01)
        
        
if __name__ == '__main__':

    unittest.main()