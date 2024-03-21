count = int(input())
x = []
y = []
output_s = []
s = ""
for i in range(count):
    x_i,y_i = input().split()
    x.append(x_i)
    y.append(y_i)
for i in range(count):
    s = ""
    for j in range(len(x[i])):
        output = ord(y[i][j])-ord(x[i][j])
        if output < 0 : output += 26
        s += str(output)+" "
    output_s.append(s.strip())
for s in output_s:
    print("Distances: "+s)