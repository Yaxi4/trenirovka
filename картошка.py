a=int(input())
c=[]
for i in range(a):
    b=input()
    if 'соль' not in b:
        #print(b)
        c.append(b)
print(', '.join(c))

