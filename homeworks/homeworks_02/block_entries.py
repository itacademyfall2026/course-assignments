# Блокировка входа.
# Дан хронологический список попыток входа `attempts` вида `(пользователь, успешна_ли)`.
# После трёх неудачных попыток подряд пользователь блокируется, и все его дальнейшие попытки игнорируются.
# Успешный вход обнуляет счётчик неудач.

if not globals().get("testing"):  # Проверка на случай тестов
    attempts = [
        ("alice", False),
        ("bob", False),
        ("alice", False),
        ("alice", True),
        ("bob", False),
        ("bob", False),
        ("bob", True),
        ("charlie", False),
        ("charlie", False),
        ("charlie", False),
        ("charlie", True),
    ]

blocked_users = []  # Сохраните результат сюда
