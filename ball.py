b=int(input())
boys=list(map(int,input().split()))
g=int(input())
girls=list(map(int,input().split()))
boys.sort()
girls.sort()
i=0
j=0
count=0
while b>i and g>j:
    if abs(boys[i]-girls[j])<=1:
        count+=1
        i+=1
        j+=1
    elif boys[i]<girls[j]:
        i+=1
    else:
        j+=1
print(count)