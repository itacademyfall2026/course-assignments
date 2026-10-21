def validate_schedule():
    """
    Проверяет расписание на наличие свободных окон и конфликтов двух событий.
    Если есть свободное окно - возвращает True, нет - False, конфликт - ValueError:

    >>> validate_schedule((8, 10), (10, 13), (14, 17))
    True
    >>> validate_schedule((8, 10), (10, 12), (12, 13), (13, 15), (15, 17))
    False
    >>> validate_schedule((8, 10), (9, 11), (11, 13), (13, 15), (16, 17))
    Traceback (most recent call last):
        ...
    ValueError: Конфликт в расписании
    """
