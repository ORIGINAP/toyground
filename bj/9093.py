import sys
input = sys.stdin.readline
count = int(input())
sentence = []
for i in range(count):
    s_i = input().split()
    sentence.append(s_i)
output = []
for i in sentence:
    temp = []
    for j in i:
        out = list(reversed(j))
        out = ''.join(out)
        temp.append(out)
    output.append(" ".join(temp))
for i in output:
    print(i)