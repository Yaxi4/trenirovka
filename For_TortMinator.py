a = []
b=[]
count=0
r, c = map(int, input().split())
for i in range(r):
    a.append(input())
for i in range(r):
    b.append([False]*c)

for i in range(r):
    if 'S' not in a[i]:
        for j in range(c):
            b[i][j]=True
for j in range(c):
    is_find=False
    for i in range(r):
        if a[i][j]=='S':
            is_find=True
            break
    if not is_find:
        for i in range(r):
            b[i][j]=True
for i in range(r):
    for j in range(c):
        if b[i][j]==True:
            count+=1


print(count)