
#Задание 1

'''a = float(input('Введите число:'))

if a > 0:
    print('Число положительное')
elif a < 0:
    print('Число отрицательное')
else:
    print('Число равно нулю')
    
# Задание 2

a = int(input('Введите число:'))

if a % 2 == 0:
    print('Чётное')
else:
    print('Нечётное')
    
# Задание 3

a = int(input('Введите число:'))
b = int(input('Введите число:'))

if a > b:
    print(a, 'больше')
elif a < b:
    print(b, 'больше')
else:
    print('Числа равны')
    
# Задание 4

a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))

if a > b and a > c:
    print(a, 'больше')
elif a < b and c < b:
    print(b, 'больше')
else:
    print(c, 'больше')'''
    
# Задание 5

'''a = float(input('Введите число:'))
b = float(input('Введите число:'))

op = input('Операция:')

if op == '+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    if a == 0:
        print('error')
    elif b == 0:
        print('error')
    else:
        print(a/b)
else:
    print('Операция не известна')'''
    
    #Задание 6
    
'''a = int(input('Введите число:'))

if a % 4 == 0 and not a % 100 == 0 or a % 400 == 0:
    print('Высокосный')
else:
    print('Не выскокосный')'''
    
    #Задание 7
    
'''a = int(input('Введите число:'))
b = int(input('Введите число:'))
c = int(input('Введите число:'))

if a + b > c and a + c > b and b + c > a:
    print("Треугольник существует.")
    
    
    if a == b == c:
        print("Тип: равносторонний")
    elif a == b or b == c or a == c:
        print("Тип: равнобедренный")
    else:
        print("Тип: разносторонний")
else:
    print("Треугольник составить нельзя.")'''
    
# Задание 8

'''a = int(input('Введите число от 0 до 100:'))

if a >= 90 and a <= 100:
    print('Отлично')
elif a >= 75 and a <=89:
    print('Хорошо')
elif a >= 60 and a <=74:
    print('Удовлетворительно')
elif a >= 0 and a <=59:
    print('Неудовлетворительно')
else:
    print('Ошибка')'''
    
# Задание 9

'''base_price = 500
age = int(input('Введите возраст: '))
day = int(input('Введите день недели (1 - пн, ..., 7 - вс): '))

discount = 0

if age < 12:
    discount -= 0.50
elif age >= 65:
    discount -= 0.30

if day == 6 or day == 7:
    discount += 0.20

final_price = base_price * (1 + discount)

print('Итоговая цена билета:', final_price, 'руб')'''

# Задание 10

password = input("Введите пароль для проверки: ")

errors = []

if len(password) < 8:
    errors.append("Длина пароля должна быть не менее 8 символов.")

if errors:
    print("Найдены следующие проблемы:")
    for error in errors:
        print(error)
else:
    print("Поздравляем! Ваш пароль надёжный.")
