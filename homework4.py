#4 homework
'''
Написать функцию для вычисления суммы всех элементов вложенных списков.
Пример списка (синтаксис Python): [1, 2, [2, 4, [[7, 8], 4, 6]]], сумма элменетов - 34
Функция должна быть рекурсивной, то есть она должна обходить каждый элемент списка и 
вызывать саму себя, если текущий элемент так же является списком. 

'''

from functools import reduce

l = [1, 2, 3, 4, [5, 6, 7, [8, 9, 10, [100, 200, [300, 400, 45]]]]]
new_l = l

def extract(my_list):
    for i in range(0, len(my_list)):
        if type(my_list[i]) == list:
            new_list = my_list[i]
            my_list.pop(i)
            for i in new_list:
                my_list.append(i)
                extract(my_list)

extract(new_l)

print(reduce(lambda x, y: x + y, l)) 