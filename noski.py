a,b=map(int,input().split())
c=0
while a>0:
    c+=1
    a-=1
    if c%b==0:
        a+=1
print(c)