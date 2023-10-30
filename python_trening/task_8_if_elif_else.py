num = 12
#num = -5
#num = 0

if num >= 0:
    print('Число больше нуля')
else:
    print('Число отрицательное')


str_1 = 'test'
str_2 = 'test1'

if str_2 >= str_1:
    print('ДА')
else:
    print('НЕТ')


num_float = 25

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Отрицательное число')

permit_print = True

if num > 0 and permit_print:
    print('num - Положительное число')
elif not permit_print:
    print('Печать запрещена')

step = 4

if step >= 1 and step == 4:
    print('Бакалавр')
elif step >= 5 and step == 6:
    print('Магистр')
else:
    print('Аспирант')


number_n = 250

if number_n >= 100 or number_n <= -100:
    print('-')
else:
    print('+')