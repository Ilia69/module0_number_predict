def binary_search(left_edge, right_edge, number):
    '''Реализует подсчёт числа шагов при поиске number в отрезке
       [left_edge, right_edge] при помощи двоичного поиска'''
    count = 1
    left = left_edge
    right = right_edge
    predict = round((right - left) / 2)

    if (left == number) or (right == number):
        return count # Проверяем левую и правую границы

    while number != predict:
        count += 1
        if predict < number:
            left = predict
            predict += round((right - left) / 2)
        elif predict > number:
            right = predict
            predict -= round((right - left) / 2)
    return count # Выход из цикла, если угадали


def recursive_binary_search(left_ed, right_ed, number, count=0):
    '''Реализует подсчёт числа шагов при поиске number в отрезке
        [left_edge, right_edge] при помощи рекурсивного двоичного поиска'''
    left = left_ed
    right = right_ed
    predict = left + round((right - left) / 2)
    count += 1

    # К проверке границ добавлена проверка
    # текущего числа для гарантии выхода из рекурсии
    if (number == left) or (number == right) or (number == predict):
        return count

    # Если число не угадано, то запускаем данную функцию
    # в том диапазоне, в котором находится искомое число
    if number < predict:
        right = predict
        return recursive_binary_search(left, right, number, count)
    elif number > predict:
        left = predict
        return recursive_binary_search(left, right, number, count)