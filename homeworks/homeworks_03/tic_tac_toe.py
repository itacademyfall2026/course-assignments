def find_tic_tac_toe_winner():
    """
    Определяет победителя на поле для крестиков-ноликов размером 3 на 3.
    Победой считаются три одинаковых непустых символа в строке, столбце
    или на диагонали. Символ пустой клетки по умолчанию — точка.
    Если победителя нет, возвращается None. Если победили сразу два разных
    игрока, вызывается ValueError. Поле неправильного размера тоже вызывает ошибку.

    >>> find_tic_tac_toe_winner(['XOX', 'OX.', 'O.X'])
    'X'
    >>> find_tic_tac_toe_winner(['XOX', 'OOO', 'X.X'])
    'O'
    >>> find_tic_tac_toe_winner(['XOX', 'OXO', 'OX.']) is None
    True
    >>> find_tic_tac_toe_winner(['XXX', 'OOO', '...'])
    Traceback (most recent call last):
        ...
    ValueError: На поле несколько победителей
    """
