a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
while b > 0:
    c = a%b
    a = b
    b = c
print(f'Нод={a}')