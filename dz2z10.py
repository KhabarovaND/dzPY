#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть.
#5 -> 1 0 1 1 0
#2
n = int(input("введите количество монет: "))
a = 0
b = 0
for i in range(n):
    x = int(input('орел или решка?: '))
    if x == 0:
        a += 1 
    else:
        b += 1
if a < b:
    print( a, 'монет нужно перевернуть')  
else:
    print( b, 'монет нужно перевернуть')   


