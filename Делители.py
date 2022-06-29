n=int(input())
count=0
for i in range(n+1,2*n):
    if i%2==0 and i!=2 or i==1:
        continue
    d=3
    c=True
    while d*d<=i:
        if i%d==0:
            c=False
            break
        d+=2
    if c:
        count+=1

print(count)
