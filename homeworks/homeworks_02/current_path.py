# Адрес рабочего каталога.
# Дан текущий абсолютный каталог формата `current_path` типа `/foo/bar/baz`.
# Дан список параметров `cd_params` для консольной команды `cd`:
# `.` - остаемся в текущем каталоге.
# `..` - переходим на уровень выше (`/foo/bar`)
# Корневой путь - "/", выше него подняться нельзя.
# Остальные значения означают переход на уровень ниже (
# `qwerty` -> `/foo/bar/baz/qwerty`,
# `abc/def` -> `/foo/bar/baz/qwerty/abc/def`,
# `/abra/cadabra` -> `/abra/cadabra`,
# ).
# Определите каталог, в котором будет действовать консоль после всех операций.

if not globals().get("testing"):  # Проверка на случай тестов
    current_path = "/home/student/projects/python"
    cd_params = ["..", "homeworks/lesson_02", ".", "../../tests", "/tmp/data", ".."]

final_path = ""  # Сохраните результат сюда
