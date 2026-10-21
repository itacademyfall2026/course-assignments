import csv
from pathlib import Path

def process_editor_events():
    """
    Превращает список событий текстового редактора в готовый текст.
    add добавляет строку, undo отменяет последнюю несохраненную строку,
    save сохраняет все несохраненные строки.
    Строки склеиваются символом переноса на новую строку:

    >>> process_editor_events([
    ... {"action": "add", "data": "A"},
    ... {"action": "add", "data": "B"},
    ... {"action": "save", "data": ""},
    ... {"action": "add", "data": "C"},
    ... {"action": "undo", "data": ""},
    ... {"action": "save", "data": ""},
    ... {"action": "add", "data": "D"},
    ... ])
    'A\\nB'
    """


def main():
    """
    Читает список событий из CSV файла (разделитель ;), обрабатывает события
    и сохраняет результат в файл.
    """


if __name__ == "__main__":
    data_dir = Path(__file__).parent / "data" / "editor"
    sample_csv = data_dir / "samples" / "1.csv"
    result_txt = data_dir / "expected" / "1.txt"

    main(sample_csv, result_txt)
