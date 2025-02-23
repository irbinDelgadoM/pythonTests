import unittest
from unittest.mock import patch
import pytest

from app.calc import Calculator


def mocked_validation(*args, **kwargs):
    return True


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # Pruebas para suma
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(0, self.calc.add(-2, 2))
        self.assertEqual(1, self.calc.add(1, 0))
        self.assertEqual(4.5, self.calc.add(3, 1.5))
        self.assertEqual(0, self.calc.add(0, 0))
        self.assertEqual(-7, self.calc.add(-2, -5))

    def test_add_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "2", "2")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())
        self.assertRaises(TypeError, self.calc.add, None, None)

    # Pruebas para resta
    def test_subtract_method_returns_correct_result(self):
        self.assertEqual(2, self.calc.subtract(5, 3))
        self.assertEqual(0, self.calc.subtract(2, 2))
        self.assertEqual(4, self.calc.subtract(2, -2))
        self.assertEqual(-4, self.calc.subtract(-2, 2))
        self.assertEqual(0, self.calc.subtract(-2, -2))
        self.assertEqual(1, self.calc.subtract(1, 0))
        self.assertEqual(1.5, self.calc.subtract(5, 3.5))
        self.assertEqual(-1.5, self.calc.subtract(3.5, 5))
        self.assertEqual(-1, self.calc.subtract(0, 1))

    def test_subtract_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.subtract, "2", 2)
        self.assertRaises(TypeError, self.calc.subtract, 2, "2")
        self.assertRaises(TypeError, self.calc.subtract, "2", "2")
        self.assertRaises(TypeError, self.calc.subtract, None, 2)
        self.assertRaises(TypeError, self.calc.subtract, 2, None)
        self.assertRaises(TypeError, self.calc.subtract, object(), 2)
        self.assertRaises(TypeError, self.calc.subtract, 2, object())

    # Pruebas para multiplicación
    def test_multiply_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-2, 0))
        self.assertEqual(0, self.calc.multiply(0, 1))
        self.assertEqual(0, self.calc.multiply(0, -2))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertEqual(-6, self.calc.multiply(3, -2))
        self.assertEqual(5, self.calc.multiply(-1, -5))
        self.assertEqual(0, self.calc.multiply(0, 0))

    def test_multiply_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.multiply, "2", 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, "2")
        self.assertRaises(TypeError, self.calc.multiply, "2", "2")
        self.assertRaises(TypeError, self.calc.multiply, None, 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, None)
        self.assertRaises(TypeError, self.calc.multiply, object(), 2)
        self.assertRaises(TypeError, self.calc.multiply, 2, object())

    # Pruebas para división
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))

    def test_divide_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "2", "2")
        self.assertRaises(TypeError, self.calc.divide, 2, "")
        self.assertRaises(TypeError, self.calc.divide, "", 2)
        self.assertRaises(TypeError, self.calc.divide, "", "")

    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(ZeroDivisionError, self.calc.divide, 2, 0)
        self.assertRaises(ZeroDivisionError, self.calc.divide, 0, 0)

    # Pruebas para potenciación
    def test_power_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.power(2, 2))
        self.assertEqual(1, self.calc.power(5, 0))
        self.assertEqual(0.25, self.calc.power(2, -2))
        self.assertEqual(-8, self.calc.power(-2, 3))
        self.assertEqual(1, self.calc.power(0, 0))
        self.assertEqual(0, self.calc.power(0, 2))

    def test_power_method_fails_with_nan_parameter(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")

    # Pruebas para raíz cuadrada
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(3, self.calc.sqrt(9))
        self.assertEqual(0, self.calc.sqrt(0))
        self.assertEqual(2.23606797749979, self.calc.sqrt(5))
        self.assertEqual(1, self.calc.sqrt(1))

    def test_sqrt_method_fails_with_nan_or_negative_parameter(self):
        self.assertRaises(TypeError, self.calc.sqrt, "9")
        self.assertRaises(ValueError, self.calc.sqrt, -9)

    # Pruebas para logaritmo en base 10
    def test_log10_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.log10(10))
        self.assertEqual(2, self.calc.log10(100))
        self.assertEqual(0, self.calc.log10(1))

    def test_log10_method_fails_with_nan_or_non_positive_parameter(self):
        self.assertRaises(TypeError, self.calc.log10, "10")
        self.assertRaises(ValueError, self.calc.log10, -10)
        self.assertRaises(ValueError, self.calc.log10, 0)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()