a: int = 5
b: str = 'Строка'
c: list = [1, 2]

def indent(s: str, width: int) -> str:
    return " " *(max(0, width - len(s))) + s

print(indent('123', 123))



def string_leight(s: str = '') -> int:
    return len(s)
print(string_leight('Пятьсотпятьдесятдевять'))

def max_list(a: list, b: list) -> int:
    return max(len(a),len(b))
print(max_list((2,3,4,5), (6,7,8,9,10,15,55)))

def dif_list(my_list: list):
    my_list.append('test')
    return my_list
print(dif_list(['один', 2, 3]))

def summ_list (my_list: list) -> int:
    result = 0
    for elem in my_list:
        result = result +elem
    return result
print(summ_list([1, 2, 3]))
