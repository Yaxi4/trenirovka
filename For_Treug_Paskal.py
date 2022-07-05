n=int(input())
treug=[]
for i in range(n+1):
    treug.append([1]+[0]*n)
for i in range(1,n+1):
    for j in range(1,i+1):
        treug[i][j]=treug[i-1][j]+treug[i-1][j-1]
print(treug)