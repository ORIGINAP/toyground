import sys
count = int(input())
a=[]
b=[]
for i in range(count):
    a_i, b_i = map(int,sys.stdin.readline().split())
    a.append(a_i)
    b.append(b_i)
for i in range(count):
    print(a[i]+b[i])