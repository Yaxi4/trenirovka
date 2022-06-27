a=int(input())
count=0
b=0
z=0
while a>z:
    count+=1
    b=count+b
    z+=b
if a==z:
    print(count)
else:
    print(count-1)