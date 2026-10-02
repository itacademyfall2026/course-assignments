# Домашние задания курса

В репозитории находятся домашние задания и мини-проекты курса. Файлы с
заданиями расположены в каталоге [`homeworks`](homeworks/README.md), а тесты — в
Git submodule `tests`.

Условия задач приведены в комментариях внутри файлов. Комментарии можно
удалять, но сами файлы нельзя переименовывать: тесты ищут решения по исходным
путям и именам.

## Требования

Для работы понадобятся:

- Git;
- Python (лучше ориентироваться на версию 3.13);
- учётная запись GitHub;

## Клонирование репозитория

Замените `<username>` на своё имя пользователя GitHub и клонируйте приватный
репозиторий вместе со всеми submodule:

```bash
git clone --recurse-submodules git@github.com:itacademyfall2026/course-assignments-<username>.git course-assignments
cd course-assignments
```

Если репозиторий уже был клонирован без submodule, инициализируйте их отдельно:

```bash
git submodule update --init --recursive
```

## Виртуальное окружение и зависимости

Создайте виртуальное окружение в корне проекта.

Для macOS или Linux:

```bash
python3.13 -m venv .venv
source .venv/bin/activate
```

Для Windows PowerShell:

```powershell
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
```

Установите зависимости для запуска тестов:

```bash
python -m pip install --require-hashes -r requirements/tests.txt
```

Проверьте решения локально:

```bash
python -m pytest
```

## Получение новых заданий

Перед началом каждого домашнего задания обновите ветку `main`. Сначала
убедитесь, что текущие изменения сохранены в commit или отсутствуют, затем
выполните:

```bash
git switch main
git pull --ff-only origin main
git fetch upstream
git merge upstream/main
git submodule sync --recursive
git submodule update --init --recursive
git push origin main
```

Если во время `merge` возникли конфликты, разрешите их перед созданием ветки с
домашним заданием. Не изменяйте содержимое каталога `tests` и не добавляйте его
в commit вручную.

## Ветки для домашних заданий

Для каждого домашнего задания создавайте отдельную ветку от обновлённой
`main`:

```bash
git switch -c feature/homework-N
```

`N` — номер домашнего задания. Используйте номер в том же формате, что и в
названии каталога, например:

```bash
git switch -c feature/homework-01
```

После выполнения задания запустите тесты, проверьте список изменений и
отправьте ветку в приватный репозиторий:

```bash
python -m pytest
git status
git add homeworks/homeworks_01
git commit -m "Complete homework 01"
git push -u origin feature/homework-01
```

В commit должны входить только файлы текущего задания. Не добавляйте изменения
из `tests`, других домашних заданий, настроек IDE или виртуального окружения.

## Форматирование кода

Установите зависимости для форматирования и проверки кода на качество:

```bash
python -m pip install --require-hashes -r requirements/lint.txt
```

Отформатируйте Python-код с помощью Ruff:

```bash
ruff format .
```

Проверьте внесённые изменения и убедитесь, что форматирование соответствует
требованиям GitHub Actions:

```bash
git diff
ruff format --check .
```

Добавьте изменения форматирования в commit до создания pull request.

## Pull request и приёмка задания

На каждое домашнее задание создавайте отдельный pull request в приватном
репозитории:

- исходная ветка — `feature/homework-N`;
- целевая ветка — `main`;
- в описании укажите номер задания;
- в Reviewers укажите `@igorsinc`
- не создавайте новый pull request для исправлений после review — отправляйте
  новые commits в ту же ветку.

Домашнее задание считается принятым, когда:

1. проверки GitHub Actions завершились успешно;
2. все замечания преподавателя исправлены;
3. pull request получил approval преподавателя.

Объединяйте pull request с `main` только после выполнения всех трёх условий.
После новых исправлений дождитесь повторного успешного запуска проверок.
