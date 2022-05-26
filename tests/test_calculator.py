import pytest
from app.calculator import Calculator
from datetime import datetime


class TestCalc:
    def setup(self):
        self.calc = Calculator

# Позитивные тесты -------------------------------------------------------------------------------------

    @pytest.mark.parametrize('x, y , expected_result', [(10, 2, 5),
                                                        (20, 10, 2),
                                                        (30, -3, -10),
                                                        (5, 2, 2.5)])
    def test_division_good(self, x, y, expected_result):
        assert self.calc.divizion(self, x, y) == expected_result

    @pytest.mark.parametrize('x, y , expected_result', [(10, 2, 20),
                                                        (20, 10, 200),
                                                        (30, -3, -90),
                                                        (5, 2.5, 12.5)])
    def test_multiply_good(self, x, y, expected_result):
        assert self.calc.multiply(self, x, y) == expected_result

    @pytest.mark.parametrize('x, y , expected_result', [(10, 2, 8),
                                                        (20, 10, 10),
                                                        (30, -3, 33),
                                                        (5, 2.5, 2.5)])
    def test_subtraction_good(self, x, y, expected_result):
        assert self.calc.substraction(self, x, y) == expected_result

    @pytest.mark.parametrize('x, y , expected_result', [(10, 2, 12),
                                                        (20, 10, 30),
                                                        (30, -3, 27),
                                                        (5, 2.5, 7.5)])
    def test_adding_good(self, x, y, expected_result):
        assert self.calc.adding(self, x, y) == expected_result

# Негативные тесты ------------------------------------------------------------------------------------

    @pytest.mark.parametrize('expected_exception, divider, divisible', [(ZeroDivisionError, 0, 10),
                                                                        (TypeError, '2', 20)])
    def test_division_with_error(self, expected_exception, divider, divisible):
        with pytest.raises(expected_exception):
            self.calc.divizion(self, divisible, divider)

    @pytest.mark.parametrize('x, y , expected_result', [(10, 0, 22),
                                                        (20, 10, 0),
                                                        (30, -3, -1),
                                                        (5, 2.5, 0)])
    def test_multiply_error(self, x, y, expected_result):
        assert self.calc.multiply(self, x, y) != expected_result

    @pytest.mark.parametrize('x, y , expected_result', [(10, 2, 0),
                                                        (20, 10, 0),
                                                        (30, -3, 0),
                                                        (5, 2.5, 0)])
    def test_subtraction_error(self, x, y, expected_result):
        assert self.calc.substraction(self, x, y) != expected_result

    @pytest.mark.parametrize('x, y , expected_result', [(10, 2, 0),
                                                        (20, 10, 0),
                                                        (30, -3, 0),
                                                        (5, 2.5, 0)])
    def test_adding_error(self, x, y, expected_result):
        assert self.calc.adding(self, x, y) != expected_result


# Таймер -----------------------------------------------------------------------------------------------

# @pytest.fixture(autouse=True)
# def time_delta():
#     start_time = datetime.now()
#     yield
#     end_time = datetime.now()
#     print(f"\nТест шел: {end_time - start_time}")
