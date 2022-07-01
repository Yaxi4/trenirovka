n,m=map(int,input().split())
b=[]

for i in range(n):
    s = list(map(int, input().split()))
    b.append(s)
for i in range(n):
    gor=0
    for j in range(m):
        gor+=b[i][j]
        #print(b[i][j],end=' ')
    print(gor, end=' ')
print()
for i in range(m):
    vert=0
    for j in range(n):
        vert+=b[j][i]
        #print(b[i][j],end=' ')
    print(vert, end=' ')