import pytest
from app.calculator import Calculator
from data.settings import positive_data_division, positive_data_multiply,\
    positive_data_subtraction, positive_data_adding, negative_data_division, \
    negative_data_multiply, negative_data_subtraction, negative_data_adding


class TestCalc:
    def setup(self):
        self.calc = Calculator

# Позитивные тесты 16 кейсов --------------------------------------------------------------------------
    '''Строка с переменными и список кортежей с данными, которые мы передаем в переменные'''

    @pytest.mark.parametrize('x, y , expected_result', positive_data_division)
    def test_division_good(self, x, y, expected_result):
        assert self.calc.divizion(self, x, y) == expected_result

    @pytest.mark.parametrize('x, y , expected_result', positive_data_multiply)
    def test_multiply_good(self, x, y, expected_result):
        assert self.calc.multiply(self, x, y) == expected_result

    @pytest.mark.parametrize('x, y , expected_result', positive_data_subtraction)
    def test_subtraction_good(self, x, y, expected_result):
        assert self.calc.substraction(self, x, y) == expected_result

    @pytest.mark.parametrize('x, y , expected_result', positive_data_adding)
    def test_adding_good(self, x, y, expected_result):
        assert self.calc.adding(self, x, y) == expected_result

# Негативные тесты 14 кейсов -------------------------------------------------------------------------
    '''Строка с переменными и список кортежей с данными, которые мы передаем в переменные'''

    @pytest.mark.parametrize('expected_exception, divider, divisible', negative_data_division)
    def test_division_with_error(self, expected_exception, divider, divisible):
        with pytest.raises(expected_exception):
            self.calc.divizion(self, divisible, divider)

    @pytest.mark.parametrize('x, y , expected_result', negative_data_multiply)
    def test_multiply_error(self, x, y, expected_result):
        assert self.calc.multiply(self, x, y) != expected_result

    @pytest.mark.parametrize('x, y , expected_result', negative_data_subtraction)
    def test_subtraction_error(self, x, y, expected_result):
        assert self.calc.substraction(self, x, y) != expected_result

    @pytest.mark.parametrize('x, y , expected_result', negative_data_adding)
    def test_adding_error(self, x, y, expected_result):
        assert self.calc.adding(self, x, y) != expected_result


# Таймер ---------------------------------------------------------------------------------------------

# @pytest.fixture(autouse=True)
# def time_delta():
#     start_time = datetime.now()
#     yield
#     end_time = datetime.now()
#     print(f"\nТест шел: {end_time - start_time}")
