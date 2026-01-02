from datetime import datetime
import math

d=datetime.now()
print("Current Date:",d.strftime("%Y-%m-%d"))
print("Current Time:",d.strftime("%H:%M:%S"))

f=input();l=input()
print("Hello",l,f)

n=input()
print(int(n)+int(n*2)+int(n*3))

a,b,c=map(int,input().split())
print(3*(a+b+c) if a==b==c else a+b+c)

x,y=map(int,input().split())
print((x+y)**2)

p,r,t=map(int,input().split())
print(p*(1+r/100)**t)

s=input()
n=float(s) if "." in s else int(s)
print(n,type(n))

n=int(input())
print(n*(n+1)//2)

n=input()
print(sum(map(int,n)))

print(ord(input()))

print("The given input is an integer" if input().isnumeric() else "The given input is not an integer")

for _ in range(5):print("***")

print(*[i for i in range(2000,3201) if i%7==0 and i%5!=0])

for i in input().split(','):
    print(int(math.sqrt(10*int(i)/3)),end=' ')

n=int(input());c=0
for i in range(n):
    for j in range(n-i):
        print(chr(65+c+i+j),end='')
    c+=n-i-1
    print()

