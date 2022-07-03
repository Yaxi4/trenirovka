n,m=map(int,input().split())
sp=[]
max_=0
b=0
s=0
for i in range(n):
    sp.append(list(map(int,input().split())))
for i in range(n):
    s=0
    for j in range(m):
        s=sum(sp[i])
        if sp[i][j]>max_:
            max_=sp[i][j]
            stroka=i
            sum_=s
        elif sp[i][j]==max_ and sum(sp[i])>sum_:
            stroka=i
            sum_=s
        #print(max_,sum_,stroka)
print(stroka)