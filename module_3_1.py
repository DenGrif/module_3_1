# Глобальная переменная для подсчета вызовов
calls = 0

# Функция подсчитывающая вызовы остальных функций.
def count_calls():
    global calls
    calls += 1

# Функция принимает аргумент - строку и возвращает кортеж
def string_info(string):
    count_calls()
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return (length, upper, lower)

# Функция принимает два аргумента: строку и список, и возвращает True
def is_contains(string, list_to_search):
    count_calls()
    string_lower = string.lower()

    return string_lower in [s.lower() for s in list_to_search]

# Пример результата выполнения программы:
print(string_info('Capybara'))  # Ожидаемый вывод: (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  # Ожидаемый вывод: (9, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Ожидаемый вывод: True
print(is_contains('cycle', ['recycling', 'cyclic']))  # Ожидаемый вывод: False
print(calls)
