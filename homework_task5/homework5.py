#5 homework
'''
Реализовать программу-калькулятор, пользователь вводит строку с некоторым выраженим, 
которое может содержать вложенные скобки, например "(4-3)*(12+(2-1))", программа выводит 
результат вычисления. Реализовать свои функции математических операций, поместив их в отдельный модуль.
Количество вложенных выражений не ограничено.

'''
import re
from mathmodule import math
from mathmodule import splitter

def calc_elements(element):
    opened = ''
    for i in element:
        if i == '(' or i == ')':
            pass
        else:
            opened = opened + i
    return math(splitter(opened))


def replacing(expr):
    if '(' in expr or ')' in expr:
        template = '\((\d+[\+]?[\-]?[\*]?[\/]?\d+)\)'
        res = re.search(template, expr)
        new = res.group(0)
        calc = calc_elements(new)
        expr = expr.replace(new, str(calc))
        replacing(expr)
    elif '+' in expr or '-' in expr or '*' in expr or '/' in expr:
        expr = calc_elements(expr)
        print(expr)
            
replacing('(25-25)+(15+(15/5))')
