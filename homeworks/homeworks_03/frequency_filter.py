def filter_by_frequency():
    """
    Возвращает элементы, количество появлений которых попадает в заданный диапазон.
    Каждый подходящий элемент включается один раз в порядке первого появления.
    Минимальная частота по умолчанию равна 1, maximum=None означает отсутствие
    верхнего ограничения. Элементы должны быть хешируемыми.
    Если minimum меньше 1 или maximum меньше minimum, вызывается ValueError.

    >>> filter_by_frequency('a', 'b', 'a', 'c', 'b', 'a', minimum=2)
    ['a', 'b']
    >>> filter_by_frequency(1, 2, 1, 3, 2, 1, minimum=1, maximum=2)
    [2, 3]
    >>> filter_by_frequency('x', 'x', 'y', minimum=3)
    []
    >>> filter_by_frequency(1, 2, minimum=0)
    Traceback (most recent call last):
        ...
    ValueError: Некорректный диапазон частот
    """
