a ,b= map(int,input().split())
s=a
s1=b
while b > 0:
    c = a%b
    a = b
    b = c
d=s*s1/a
print(int(d))