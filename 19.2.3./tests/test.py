import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_success(self):
       assert self.calc.adding(1, 1) == 2

    def test_devision_success(self):
        assert self.calc.division(8, 2) == 4

    def test_subtraction_success(self):
       assert self.calc.subtraction(3, 1) == 2

    def test_multiply_success(self):
        assert self.calc.multiply(3, 4) == 12

    def test_adding_unsuccess(self):
        assert self.calc.adding(1, 1) == 3

    def test_zero_devision(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def teardown(self):
        print('Работа метода Teardown')






