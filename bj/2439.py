a = int(input())
b = []
for i in range(a):
    b.append("")
    for j in range(i+1):
        b[i] += "*"
for i in b:
    print(i.rjust(a))