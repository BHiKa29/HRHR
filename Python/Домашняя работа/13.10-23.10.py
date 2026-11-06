
# 1

'''a = int(input('Введите начало диапозона:'))
b = int(input('Введите конец диапозона:'))

print('Числа кратные 7 в диапазоне от', a, 'до', b, ':')

for i in range(a , b + 1):
    if i % 7 == 0:
        print(i , end=' ')'''
        
# 2

'''a = int(input('Введите начало диапозона:'))
b = int(input('Введите конец диапозона:'))'''

#Все числа диапазона

'''for i in range(a , b + 1):
    print(i, end=' ')'''
    
#В убывающем порядке

'''for i in range(b , a - 1, -1):
    print(i, end=' ')'''
    
#Все числа кратные 7

'''for i in range(a , b + 1):
    if i % 7 == 0:
        print(i , end=' ')'''
        
#Количество кратных 5

count = 0

'''for i in range(a , b + 1):
    
    if i % 5 == 0:
        count += 1
        
print(count)'''

# 3

a = int(input('Введите начало диапозона:'))
b = int(input('Введите конец диапозона:'))

for i in range(a , b + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizz Buzz')
    elif i % 3 == 0:
            print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)