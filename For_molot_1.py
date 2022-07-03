n,m=map(int,input().split()) 
mas=[]
count=0
count2=0
for i in range(n):

    mas.append(list(map(int,input().split())))
for i in range(len(mas)):
    if count<sum(mas[i]):
        count=sum(mas[i])
        b=i
print(count)
print(b)