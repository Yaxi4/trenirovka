a = int(input())
b=[]
count=0
for i in range(a):
    s = list(map(int, input().split()))
    b.append(s)
for i in range(a):
    for j in range(a):
        if i==j:
            count+=b[i][j]
print(count)