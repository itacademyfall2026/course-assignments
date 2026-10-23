import csv
from pathlib import Path


def calculate_shopping_list():
    """
    Рассчитывает покупки для меню.
    Возвращает список с кортежами с названием ингредиента и количеством упаковок.
    Количество упаковок всегда округляется вверх, а порядок
    ингредиентов - алфавитный.

    >>> recipes = {"Каша": {"Крупа": 80, "Молоко": 250}}
    >>> ingredients = {"Крупа": 400, "Молоко": 900}
    >>> menu = {"Каша": 3}
    >>> calculate_shopping_list(recipes, ingredients, menu)
    [('Крупа', 1), ('Молоко', 1)]

    Неизвестный рецепт или ингредиент, повторяющееся описание ингредиента,
    неположительный вес упаковки или неположительное количество вызывают ValueError.
    """


def transform_recipes():
    """
    Преобразует список рецептов в словарь:

    >>> recipes = [
    ...     {"recipe": "Каша", "ingredient": "Крупа", "amount": "80"},
    ...     {"recipe": "Каша", "ingredient": "Молоко", "amount": "250"},
    ... ]
    >>> transform_recipes(recipes)
    {'Каша': {'Крупа': 80, 'Молоко': 250}}
    """


def transform_ingredients():
    """
    Преобразует список ингредиентов в словарь:

    >>> ingredients = [
    ...     {"ingredient": "Крупа", "weight": "400"},
    ...     {"ingredient": "Молоко", "weight": "900"},
    ... ]
    >>> transform_ingredients(ingredients)
    {'Крупа': 400, 'Молоко': 900}
    """


def transform_menu():
    """
    Преобразует меню в словарь:

    >>> menu = [
    ...     {"day": "Понедельник", "breakfast": "Каша", "lunch": "Каша", "dinner": "Каша"}
    ... ]
    >>> transform_menu(menu)
    {'Каша': 3}
    """


def read_csv():
    """
    Читает CSV-файл с разделителем ;. Возвращает список словарей.
    """


def main():
    """
    Читает три CSV-файла с разделителем ;:

    * рецепты — поля recipe, ingredient, amount;
    * ингредиенты — поля ingredient, weight, price;
    * меню — поля day, breakfast, lunch, dinner.

    Рассчитывает количество упаковок, сохраняет список покупок в алфавитном порядке CSV-файл с
    полями ingredient и units. Выходной файл записывается с разделителем ;.
    """



if __name__ == "__main__":
    data_dir = Path(__file__).parent / "data" / "shopping_list"
    recipes_csv = data_dir / "samples" / "1" / "recipes.csv"
    ingredients_csv = data_dir / "samples" / "1" / "ingredients.csv"
    menu_csv = data_dir / "samples" / "1" / "menu.csv"
    result_csv = data_dir / "expected" / "1.csv"

    main(
        recipes_csv,
        ingredients_csv,
        menu_csv,
        result_csv,
    )
