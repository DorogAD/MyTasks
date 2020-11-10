#1 Homework
'''
Депозит:
начальная сумма - 20000 BYN
срок - 5 лет 
процент - 15%
ежемесячная капитализация

Вычислить сумму на счету в конце указанного срока.
'''

deposit = 20000
years = 5
month = 12
percents = 5

kap = 1 + ((percents / month) / 100)
deposit = round(deposit * pow(kap, (years * month)), 2)
print(deposit)
