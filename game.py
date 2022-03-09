'Игра угадай число'

import numpy as np

number = np.random.randint(1, 101)

count = 0

while True:
    count+=1
    predict_namber = int(input('Угадай число от 1 до 100: '))
    
    if predict_namber > number:
        print('Число должно быть меньше!')
    
    elif predict_namber < number:
        print('число должно быть больше!')
    
    else:
        print(f'Вы угадали число! Это число = {number}, за {count} попыток')
        break