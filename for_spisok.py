a=int(input())
spisok=[0]*10
for i in str(a):
    spisok[(int(i))]+=1
for i in range(10):
    if spisok[i]>0:
        print(i,spisok[i])
