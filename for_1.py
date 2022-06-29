a = int(input())
spisok = list(map(int, input().split()))
b = []
for i in range(a):
    b.append(min(spisok))
    spisok.remove(min(spisok))

print(*b)