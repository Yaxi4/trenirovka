n = int(input())
a = []
count=0
for i in range(n):
    b.append(list(map(int, input().split())))
for i in range(n-1):
    for j in range(i+1,n):
        if a[i][0]==a[j][1]:
            count+=1
        if a[i][1]==a[j][0]:
            count+=1
print(count)


