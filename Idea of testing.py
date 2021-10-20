import random
from time import sleep

print('                                         Привет   мой    друг !')
print()
sleep(2)
print('                                           Тест начинается !')
sleep(2)
print()


def start_func():
    while True:
        user_input = input(
            'Выбери направление перевода:  №1 - c английского на русский язык ; №2 - с русского на английский язык : ')
        print()
        if user_input.isdigit():
            if int(user_input) == 1:
                sleep(1)
                print(f'Выбрано направление №1: c английского на русский язык')
                print()
                sleep(1)
                dict_f = dict_forward()
                return dict_f
            elif int(user_input) == 2:
                sleep(1)
                print(f'Выбрано направление №2: c русского на английский язык')
                print()
                sleep(1)
                dict_r = dict_reverse(dict_forward())
                return dict_r
            else:
                print('Такого варианта не существует. Допустимые значения 1 или 2.')
        else:
            print('Необходимо ввести цифры: 1 или 2.')




def guess_answer(dic):
    correct_answer = 0
    wrong_answer = 0
    total_answer = 0
    # corr_answer = None
    len_dic_all = len(dic)
    while len(dic) > 0:
        wrong_dic = {}
        list_guess = random.choice(list(dic.keys()))  # - преобразование ключей словаря в список
        print(f'Угадай слово --- "{list_guess.upper()}" ')
        user_input = input('Введите ответ : ').lower().strip()
        total_answer += 1
        if user_input == 'все' or user_input == 'end':
            sleep(1)
            print()
            print(f'Всего вопросов было : {total_answer}')
            print(f'Правильных ответов : {correct_answer}')
            print(f'Неправильных ответов: {wrong_answer}')
            print()
            print(f'Всего слов в словаре : {len_dic_all}'.upper())
            # wrong_dic[list_guess] = user_input  # - выводит как  ответил пользователь     # - это надо тут реализовать !!!!!!!!!!!!!
            # print(wrong_dic)
            # corr_answer = dic.pop(list_guess)  # - удаление пары (ключ:значение) уже заданного вопроса
            # print(f'Правильный ответ : {corr_answer}')  # - вывод правильного ответа
            print()
            print('"До новых встреч !"')
            break

        elif user_input == dic.get(list_guess):
            sleep(1)
            print()
            print('"Правильно"')
            print()
            correct_answer += 1
            sleep(1)
            dic.pop(list_guess)  # - удаление пары (ключ:значение) уже заданного вопроса

        else:
            sleep(1)
            print()
            print('"Неправильно"')
            print()
            sleep(1)
            wrong_answer += 1
            wrong_dic[list_guess] = user_input  # - выводит как  ответил пользователь
            print(wrong_dic)
            corr_answer = dic.pop(list_guess)    # - удаление пары (ключ:значение) уже заданного вопроса
            print(f'Правильный ответ : {corr_answer}')  # - вывод правильного ответа
            print()

    print('"У меня вопросов больше нет !"')
    print()
    print(f'Всего вопросов было : {total_answer}')
    print(f'Правильных ответов : {correct_answer}')
    print(f'Неправильных ответов: {wrong_answer}')
    print()
    print(f'Всего слов в словаре : {len_dic_all}'.upper())


# - c русского на английский язык
def dict_forward():  # - функция для чтения слов из файла и преобразования к единому словарю
    with open('WordBook_1.txt') as f:
        content = f.readlines()
        print()
        words_forward = {}
        for line in content:
            d = line.replace('-', '').strip().split()
            words_forward.update({d[0]: d[1]})
        return words_forward

 # - c английского на русский язык

def dict_reverse(words_forward):  # - функция для чтения слов из файла и преобразования к единому словарю(ключ-значения поменялись местами)
    words_reverse = {v: k for k, v in words_forward.items()}
    return words_reverse



def main():
    dic = start_func()
    answer = guess_answer(dic)



if __name__ == '__main__':
    main()



input()
#                                           Задачи:
# - реализовать забор например ключей (с удалением из списка), чтобы не повторялся вопрос( наверное использовать функцию pop())  '+'

# - реализовать метод забора у ключа с несколькими значениями и если значение состоит из двух слов и более например как быть

# - реализовать возможность с помощью random() выводить слова для ответа как английском, так и на русском(попеременно)

# - реализовать в конце вывод в каких словах допущена ошибка и правильный ответ на них   '+-'

# - сделать exe (из многих файлов пайтона в один)

# - сколько времени потрачено на тест(использовать модуль datetime())
