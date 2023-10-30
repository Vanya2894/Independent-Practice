def add (x, y):
    return x + y

print(add(1,2))
print(add('I a', 'm Tester'))

def agr (a, b, c=2, d=3):
    return a + b + c + d

print(agr(1, 1, 1, 1))
print(agr(2, 2))
print(agr(2, 2, 1, 1))

def renge_agr(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(renge_agr('1', '2', '3', '4'))
print(renge_agr('1', '2', d='3', c='4'))


def one_arg(a=(1, 2, 3, 4)):
    return a[1]

print(one_arg())


def two_arg(radius, pi = 3.14159):
    return pi * radius * radius

print(two_arg(2))


