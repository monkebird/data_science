import numpy as np

def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0  # Счетчик попыток
    max_number = 100  # Верхняя граница диапазона для угадывания
    min_number = 0  # Нижняя граница диапазона для угадывания
    predict = np.random.randint(1, 101)  # Первоначальное предполагаемое число выбирается случайно в диапазоне от 1 до 100
    
    while number != predict:
        count += 1
        if number > predict:
            min_number = predict + 1  # Обновляем нижнюю границу диапазона
            predict = (max_number + min_number) // 2  # Выбираем новое предполагаемое число как среднее значение диапазона
        elif number < predict:
            max_number = predict - 1  
            predict = (max_number + min_number) // 2

    return count  # Возвращаем количество попыток, потребовавшихся для угадывания числа

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)