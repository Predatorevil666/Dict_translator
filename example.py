row = 'match - спичка, совпадение'  # Одна из твоих строк

some_dict = {}  # Твой словарь со словами

key, value = row.split('-')  # Бьем строку по признаку "-" на части, и получаем key="match " и value=" спичка, совпадение"

# С помощью генератора списков получаем список возможных значений.
# Сплитим value по запятой, и у каждого получившегося значения вызываем метод strip() для удаления лишних проблеов.
# В итоге имеет вид values=['спичка', 'совпадение']
values = [val.strip() for val in value.split(',')]

# Помещаем в накопительный словарь полученные данные.
# Ключу с вызванным методом strip() присваиваем значение списка values=['спичка', 'совпадение']
# В итоге имеет такую запись в словаре: {'match': ['спичка', 'совпадение']}
some_dict[key.strip()] = values

current_question = some_dict.get('match')  # По ключу получаем из словаря список вариантов ответов.

user_input = input(f'Как переводится слово match: ').lower().strip()  # Обрабатываем пользовательский ввод.

# Выясняем, есть ли то, что ввёл пользователь в списке хранящихся вариантов к данному ключу.
if user_input in current_question:
    print('Правильно!')  # Если да, то ответ правильный
else:
    print('Твой ответ неправильный!')  # Иначе ответ неверный