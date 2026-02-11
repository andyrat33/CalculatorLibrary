"""
Unit tests for the calculator library
"""
import pytest
import calculator


class TestCalculator:
    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiplication(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 100 == calculator.divide(200, 2)
        assert 9 == calculator.divide(20, 2.1)

    def test_division_by_zero(self):
        with pytest.raises(ValueError):
            calculator.divide(10, 0)

    def test_divide_fl(self):
        assert 9.523809523809524 == calculator.divide_fl(20, 2.1)

    def test_divide_fl_by_zero(self):
        with pytest.raises(ValueError):
            calculator.divide_fl(10, 0)

    def test_squared(self):
        assert 25 == calculator.square(5)

    def test_cubed(self):
        assert 125 == calculator.cube(5)

    def test_power(self):
        assert 4 == calculator.power(4, 1)

    def test_modulus(self):
        assert 1 == calculator.mod(5, 2)

    def test_modulus_by_zero(self):
        with pytest.raises(ValueError):
            calculator.mod(5, 0)

    def test_sqroot(self):
        assert 2 == calculator.square_root(4)

    def test_itob(self):
        assert "0b10" == calculator.itob(2)
        with pytest.raises(TypeError):
            calculator.itob("a")
        assert "0b11" == calculator.itob(3)
