b=int(input())
a=list(map(int,input().split()))
count=0
while b>0:
    b-=1
    for i in range(b):
        while a[i+1]<a[i]:
            a[i+1],a[i]=a[i],a[i+1]

print(*a)
