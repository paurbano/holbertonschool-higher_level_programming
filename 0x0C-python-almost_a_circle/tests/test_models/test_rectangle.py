#!/usr/bin/python3
"""Unittest for base.py"""

from models.base import Base
from models.rectangle import Rectangle
import unittest
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):
    """unnittest"""

    def setUp(self):
        """ Put stdout and set rectangles"""
        self.old_stdout = sys.stdout
        sys.stdout = self.mystdout = StringIO()
        self.g1 = Rectangle(10, 2)
        self.g2 = Rectangle(2, 10)
        self.g3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self):
        sys.stdout = self.old_stdout

    def test_excep(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")

    def test_A(self):
        """Test id"""
        self.assertEqual(self.g1.id, 51)
        self.assertEqual(self.g2.id, 52)
        self.assertEqual(self.g3.id, 12)
        """ Test width"""
        self.assertEqual(self.g1.width, 10)
        self.assertEqual(self.g2.width, 2)
        self.assertEqual(self.g3.width, 10)
        """ Test height"""
        self.assertEqual(self.g1.height, 2)
        self.assertEqual(self.g2.height, 10)
        self.assertEqual(self.g3.height, 2)
        """ Test x"""
        self.assertEqual(self.g1.x, 0)
        self.assertEqual(self.g2.x, 0)
        self.assertEqual(self.g3.x, 0)
        """ Test y"""
        self.assertEqual(self.g1.y, 0)
        self.assertEqual(self.g2.y, 0)
        self.assertEqual(self.g3.y, 0)
        """ Test area"""
        self.assertEqual(self.g1.area(), 20)
        self.assertEqual(self.g2.area(), 20)
        self.assertEqual(self.g3.area(), 20)

    def test_B_someExecp(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2)
            r1.width = - 10
            self.g1.width = - 10
            self.g2.width = - 10
            self.g3.width = - 10

        with self.assertRaises(ValueError):
            r2 = Rectangle(10, 2)
            r2.height = - 10
            self.g1.height = - 10
            self.g2.height = - 10
            self.g3.height = - 10

        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 2)
            r3.x = - 10
            self.g1.x = - 10
            self.g2.x = - 10
            self.g3.x = - 10

    def test_01(self):
        """Test 1 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(float("nan"), 1)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))

    def test_02(self):
        """Test 2 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(float("inf"), 1)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))

    def test_03(self):
        """Test 3 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(12)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

    def test_04(self):
        """Test 4 for Rectangle"""
        r = Rectangle(20, 4)
        self.assertEqual(r.id, 11)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_05(self):
        """Test 5 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(None)
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'height'",
            str(e.exception))

    def test_06(self):
        """Test 6 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        self.assertEqual(
            "__init__() missing 2 required positional arguments:" +
            " 'width' and 'height'",
            str(e.exception))

    def test_07(self):
        """Test 7 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(22, "32")
        self.assertEqual(
            "height must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle("10", 2)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r8 = Rectangle(10, 2, "3")
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2, 0, "lol")
        self.assertEqual(
            "y must be an integer",
            str(e.exception))

    def test_08(self):
        """Test 8 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 24.1)
        self.assertEqual(
            "height must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(9.12, 2)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(12, 3, 6.7859)
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(12, 3, 0, 6123.5)
        self.assertEqual(
            "y must be an integer",
            str(e.exception))

    def test_09(self):
        """Test 9 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, [])
        self.assertEqual(
            "height must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle([1, 2, 3], 2)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2, [[3, 4]])
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(12, 2, 0, ["test"])
        self.assertEqual(
            "y must be an integer",
            str(e.exception))

    def test_10(self):
        """Test 10 for Rectangle"""
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, {})
        self.assertEqual(
            "height must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle({"3": 3, "2": 4, "1": 5}, 2)
        self.assertEqual(
            "width must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(10, 2, {"a": 1})
        self.assertEqual(
            "x must be an integer",
            str(e.exception))
        with self.assertRaises(TypeError) as e:
            r = Rectangle(22, 2, 0, {"test": None})
        self.assertEqual(
            "y must be an integer",
            str(e.exception))

    def test_12(self):
        """Test 11 for Rectangle"""
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -27)
        self.assertEqual(
            "height must be > 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(-1, -23)
        self.assertEqual(
            "width must be > 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -11)
        self.assertEqual(
            "x must be >= 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 5, -167)
        self.assertEqual(
            "y must be >= 0",
            str(e.exception))

    def test_13(self):
        """Test 13 for Rectangle"""
        with self.assertRaises(ValueError) as e:
            r = Rectangle(7, 0)
        self.assertEqual(
            "height must be > 0",
            str(e.exception))
        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 22)
        self.assertEqual(
            "width must be > 0",
            str(e.exception))
        r = Rectangle(11, 21, 0, 0)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)


if __name__ == "__main__":
    unittest.main()
