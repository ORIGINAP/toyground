s = []
while True:
    s_i = input()
    if(s_i)=="END": break
    s.append(s_i)
for i in s:
    output = list(i)
    output.reverse()
    print("".join(output))