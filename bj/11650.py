import sys
count = int(sys.stdin.readline())
vec = []
for i in range(count):
    x_i, y_i = map(int,sys.stdin.readline().split())
    vec.append([x_i,y_i])
vec = sorted(vec, key=lambda x:(x[0],x[1]))
for c in vec:
    c = map(str,c)
    print(" ".join(c))