a=int(input())
sum_=[]
for i in range(a-1,0,-1):
    if i%3==0 or i%5==0:
        sum_.append(i)
print(sum(sum_))