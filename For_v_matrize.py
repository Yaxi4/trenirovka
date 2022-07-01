a=5
b=[]
count=0
for i in range(a):
    s = list(map(int, input().split()))
    b.append(s)
for i in range(a):
    for j in range(a):
        if b[i][j]==1:
            goriz=i
            vertik=j
print(abs(2-goriz)+abs(2-vertik))