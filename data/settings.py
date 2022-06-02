# Данные для позитивных тестов
positive_data_division = [
    (10, 2, 5),
    (20, 10, 2),
    (30, -10, -3),
    (30, 2.5, 12)
]

positive_data_multiply = [
    (10, 2, 20),
    (20, 10, 200),
    (30, -3, -90),
    (5, 2.5, 12.5)
]

positive_data_subtraction = [
    (10, 2, 8),
    (20, 10, 10),
    (30, -3, 33),
    (5, 2.5, 2.5)
]

positive_data_adding = [
    (10, 2, 12),
    (20, 10, 30),
    (30, -3, 27),
    (5, 2.5, 7.5)
]

# Данные для негативных тестов
negative_data_division = [
    (ZeroDivisionError, 0, 10),
    (TypeError, '2', 20)
]

negative_data_multiply = [
    (10, 0, 22),
    (20, 10, 0),
    (30, -3, -1),
    (5, 2.5, 0)
]

negative_data_subtraction = [
    (10, 2, 0),
    (20, 10, 0),
    (30, -3, 0),
    (5, 2.5, 0)
]

negative_data_adding = [
    (10, 2, 0),
    (20, 10, 0),
    (30, -3, 0),
    (5, 2.5, 0)
]

