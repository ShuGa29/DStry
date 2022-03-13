"""Игра - "Угадай число", где компьютер сам загадывает число и возвращает среднее значение попыток"""
 
import numpy as np

def random_predict(number:int=1) -> int: # Функция подсчета количества попыток
   
    count = 0 # Счетчик попыток
    left_edge = 1 # Граница минимального значения
    right_edge = 101 # Граница максимального значения
        
    while True: # Проходим циклом по диапазону значений
        count += 1
        predict_number = (right_edge + left_edge) // 2 
        
        if number < predict_number: # Задаем условие для сужения дапазона поиска числа и уменьшения числа попыток
            right_edge = predict_number
            
        elif number > predict_number:
            left_edge = predict_number
            
        else:
            break
        
    return(count)

def score_game(random_randit) -> int:
    
    """Функция подсчета количества попыток, которое в среднем угадывает наш алгоритм за 1000 подходов 
    
    Args:
        random_ predict ([type]): функция угадывания числа
        
    Returns:
        int: среднее количество попыток"""
    
    count_ls = []
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # Загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__": #RUN
    score_game(random_predict)