size = int(input())
a = input().split(" ")
b = input().split(" ")
a = list(map(int,a))
b = list(map(int,b))
a.sort(reverse=True)
b.sort()
output = []
for i in range(len(a)):
    output.append(a[i]*b[i])
res = sum(output)
print(res)