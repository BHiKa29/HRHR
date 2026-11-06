

import random

secret = random.randint(1, 100)

pop = 0

print("Привет! Я загадал число от 1 до 100.")
print("\nПопробуй его угадать!")

while True:
    user = input("\nВведи число: ")
    
    if not user.isdigit():
        print("Ошибка! Пожалуйста, введи целое положительное число.")
        continue
        
    num_user = int(user)
    
    pop = pop + 1
    
    if num_user < secret:
        print("Мое число больше.")
        
    elif num_user > secret:
        print("Мое число меньше.")
        
    else:
        print('Поздравляю! Ты угадала число' , secret , '!')
        print('Количество потраченных попыток:' , pop)
        break
