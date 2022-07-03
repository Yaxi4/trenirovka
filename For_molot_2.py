n, m = map(int, input().split())
mas = []
count = 0
count2 = 0
for i in range(n):
    mas.append(list(map(int, input().split())))
for i in range(n):
    for j in range(m):
        if mas[i][j] > count:
            count = mas[i][j]
            b = i
            c = j
print(count)
print(b, c)
