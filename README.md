# Запуск скриптов на Python (Playwright)

Этот Readme объясняет, как настроить и запустить тесты с использованием Playwright и скрипт для отображения информации о массиве

## Предварительные требования

- Python 3.8 или новее
- Установленный менеджер пакетов pip

## Установка

## Проверка версии Python
```bash
python --version  # или python3 --version
```
## Установка зависимостей
Для Playwright
```bash
pip install playwright
playwright install
```
## Запуск скриптов
Python list info
```bash
python list_info.py
```
Скрипт выведет необходимую информацию о массиве (четные элементы, наибольшее и наименьшее число, отсортированный по возрастанию массив)

Playwright Test

```bash
python playwright_test.py
```
Скрипт откроет браузер, выполнит проверки и закроется

## Версии библиотек

Python	3.8+
Playwright	1.40+

## Дополнительные настройки
Headless-режим (без отображения браузера)
```python
# Playwright
browser = p.chromium.launch(headless=True)
```

Логирование ошибок
Добавьте в блок except:

```python
# Playwright
page.screenshot(path="error.png")
```
