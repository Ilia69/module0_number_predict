import numpy as np
import time
import game_core


def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))

    t0 = time.time()
    for number in random_array:
        count_ls.append(game_core(number))
    t1 = time.time()
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    print(f"Среднее время поиска {(t1-t0) / len(random_array)} секунд")

    return (score)


score_game(game_core.game_core_v4)