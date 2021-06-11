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
