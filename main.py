import numpy as np
import game_core

# def game_core_v1(number):
#     '''Просто угадываем на random, никак не используя информацию о больше или меньше.
#        Функция принимает загаданное число и возвращает число попыток'''
#     count = 0
#     while True:
#         count += 1
#         predict = np.random.randint(1, 101)  # предполагаемое число
#         if number == predict:
#             return count  # выход из цикла, если угадали
#
# def game_core_v2(number):
#     '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
#        Функция принимает загаданное число и возвращает число попыток'''
#     count = 1
#     predict = np.random.randint(1,101)
#     while number != predict:
#         count+=1
#         if number > predict:
#             predict += 1
#         elif number < predict:
#             predict -= 1
#     return count # выход из цикла, если угадали


# def binary_search(left_edge, right_edge, number):
#     '''Реализует подсчёт числа шагов при поиске number в отрезке
#        [left_edge, right_edge] при помощи двоичного поиска'''
#     count = 1
#     left = left_edge
#     right = right_edge
#     predict = round((right - left) / 2)
#
#     if (left == number) or (right == number):
#         return count # Проверяем левую и правую границы
#
#     while number != predict:
#         count += 1
#         if predict < number:
#             left = predict
#             predict += round((right - left) / 2)
#         elif predict > number:
#             right = predict
#             predict -= round((right - left) / 2)
#     return count # Выход из цикла, если угадали


# def game_core_v3(number):
#     '''Запускаем двоичный поиск на отрезке [1 , 100]'''
#     left_edge = 1
#     right_edge = 100
#     count = binary_search(left_edge, right_edge, number)
#
#     return count


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)


score_game(game_core.game_core_v3)