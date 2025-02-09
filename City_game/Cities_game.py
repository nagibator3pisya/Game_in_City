
import json

'''
Достал из сити только города и преобразовал их в сет
'''
# my_set = {city['name'] for city in cities} # новый вариант
# copy_my_set = my_set.copy()
# copy_list_set = list(copy_my_set)
#
# # сделаем файл json
#
# with open('cities.json', 'w',encoding='utf8') as f:
#     json.dump(list(copy_my_set) , f, indent=1,ensure_ascii=False)
with open('cities.json', 'r', encoding='utf8') as f:
    file = json.load(f)

copy_my_set = set(file)
copy_list_set = list(copy_my_set)


bots = copy_my_set.pop() # рандом слово от бота
print(f'Слова бота: {bots}')



bools = False

while not bools:
    user_input = input('Введите название города:').strip()
    if user_input == 'Стоп':
        print('Cтоп игра')
        break
    user_city = set(user_input.split(',')) # приобразовка в сет
    out = user_city.intersection(copy_my_set) # сравнение

    if not out:
        print('Такого города нет выиграл бот ')
        break

    str_out = ''.join(out).lower()

    if str_out[0].lower() != bots[-1].lower():
        print(f'Не правильный ответ он должен начинаться на букву {bots[0]}')
        continue

    if str_out[-1].lower() in ["ь","ъ","ы","ц","й"]:
        print('Проиграл ты ')
        break
    else:
        print(f'Бот: мне на букву {str_out[-1]}')
        dels = out.pop() # удаляет и возвращает его
        copy_my_set.remove(dels) # окончательно удаляет

        # print(f'Удаляю этот город {dels}')
        # print(len(copy_my_set))

    for i in copy_list_set:
        if i[0].lower() == str_out[-1]: # Если 1 буква бота равна последней буквы игрока
            bots = i
            copy_list_set.remove(i) # Удаляем слово из городов
            print(f'Бот : {i} , тебе на букву {i[-1]}')
            break


else:
    bools = True
    print('Ты выиграл')
