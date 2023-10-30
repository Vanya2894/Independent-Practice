a = [5, 10, 15, 25, 29, 30, 35, 40]

print('a[2] =', a[2])
print('a[0:3]= ',a[0:3])

b = [11, 12, 13]
b[2] = 4
print(b)


test_list = ['Один', 'Два', 'Три', 'Четыре', 'Пять']

for elem in test_list:   #Цикл по списку
    print(elem)

print(len(test_list)) # Получить длину списка

test_list.append('Шесть')  #Добавить значение в список
print(test_list)
