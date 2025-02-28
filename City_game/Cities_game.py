#
# import json
#
# '''
# Достал из сити только города и преобразовал их в сет
# '''
# # my_set = {city['name'] for city in cities} # новы вариант
# # copy_my_set = my_set.copy()
# # copy_list_set = list(copy_my_set)
# #
# # # файл json
# #
# # with open('cities.json', 'w',encoding='utf8') as f:
# #     json.dump(list(copy_my_set) , f, indent=1,ensure_ascii=False)

# with open('cities.json', 'r', encoding='utf8') as f:
#     file = json.load(f)
#
# copy_my_set = set(file)
# copy_list_set = list(copy_my_set)
#
#
# bots = copy_my_set.pop() # рандом слово от бота
# print(f'Слова бота: {bots}')
#
#
#
# bools = False
#
# while not bools:
#     user_input = input('Введите название города:').strip()
#     if user_input == 'Стоп':
#         print('Cтоп игра')
#         break
#     user_city = set(user_input.split(',')) # приобразовка в сет
#     out = user_city.intersection(copy_my_set) # сравнение
#
#     if not out:
#         print('Такого города нет выиграл бот ')
#         break
#
#     str_out = ''.join(out).lower()
#
#     if str_out[0].lower() != bots[-1].lower():
#         print(f'Не правильный ответ он должен начинаться на букву {bots[0]}')
#         continue
#
#     if str_out[-1].lower() in ["ь","ъ","ы","ц","й"]:
#         print('Проиграл ты ')
#         break
#     else:
#         print(f'Бот: мне на букву {str_out[-1]}')
#         dels = out.pop() # удаляет и возвращает его
#         copy_my_set.remove(dels) # окончательно удаляет
#
#         # print(f'Удаляю этот город {dels}')
#         # print(len(copy_my_set))
#
#     for i in copy_list_set:
#         if i[0].lower() == str_out[-1]: # Если 1 буква бота равна последней буквы игрока
#             bots = i
#             copy_list_set.remove(i) # Удаляем слово из городов
#             print(f'Бот : {i} , тебе на букву {i[-1]}')
#             break
#
#
# else:
#     bools = True
#     print('Ты выиграл')

import json
from typing import List, Set
from setting_game import *


#
def hello_game_func():
    pass


def reid_file_json(encoding = 'utf8') -> List:
    with open('cities.json', 'r', encoding=encoding) as f:
        file = json.load(f)
    return file


def bot_city_file(file_city_json):
    '''
    Бот берет города из дата сета
    :param file_city_json: бот принимает файл с городами
    :return: возврат рандомного города из сета
    '''
    set_city = set(file_city_json)
    copy_set_city_json = set_city.copy()
    bots = copy_set_city_json.pop()
    return f"{MESSEG_BOT} {bots}", copy_set_city_json




def user_motion(copys_set_json:Set[str]) -> str:
    """
    Ход для пользователя,
    :param copys_set_json: сравнение с сетом
    :return: str_out, для того что бы сравнить с ботом и дать след. слово
    """
    bools = False
    while not bools:
        user_input = input('Введите название города: ').strip()
        if user_input == 'Стоп':
            print('Конец игры')
            break
        user_city = set(user_input.split(',')) # приобразовка в сет
        out = user_city.intersection(copys_set_json) # сравнение
        if not out:
            print(f'{LOST_THE_GAME_USER}, такого города нет')
            break
        str_out = ''.join(out).lower()
        return str_out


def bot_motion(str_out_user_last: str, copys_set_json: Set[str]) -> str:

        last_letter = str_out_user_last[-1]
        print(f'Бот: мне на букву {last_letter}')
        for city in copys_set_json:
            if city[0].lower() == last_letter:
                bot = city
                copys_set_json.remove(city) # Удаляет город из множеств
                print(f'{MESSEG_BOT} {bot} тебе на букву {bot[-1]}')
                return bot
        print(f"{LOST_THE_GAME_BOT}")





def check_bot_filter_letter(bot_str):
    # for i in bot_str:
    pass
#
#
#
#
# """
# ЭТО писал чат
# """
file = reid_file_json()
bot_message, copys_set_json = bot_city_file(file)
print(bot_message)


while True:
    user_city = user_motion(copys_set_json)
    if not user_city:
        break
    test = check_user_letter(user_city)
    if test:
        break
    bot_city = bot_motion(user_city, copys_set_json)
    if not bot_city:
        break





















