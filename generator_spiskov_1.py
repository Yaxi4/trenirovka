from string import ascii_uppercase
a=int(input())
b=[ascii_uppercase[i]*(i+1) for i in range(a)]
print(b)