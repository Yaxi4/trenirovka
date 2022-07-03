n,m=map(int,input().split())
a=[]
count=0
max_=0
s=0
for i in range(n):
    a.append(list(map(int,input().split())))
for i in range(n):
    for j in range(m):
        if a[i][j]>max_:
            max_=a[i][j]
            count=i
            s=1
        if a[i][j]==max_ and count!=i:
            count=i
            s+=1
print(s)