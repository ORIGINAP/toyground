import sys
input = sys.stdin.readline
count = int(input())
vec = []

def find_divisor(n):
    i = 1
    divisor = []
    temp = []
    while True:
        if i*i<n:
            if(n%i==0):
                temp.append(i)
                divisor.append(i)
        else:
            break
        i+=1
    for c in (temp):
        divisor.append(int(n/c))
    return divisor

for i in range(count):
    vec_i = list(map(int,input().split()))
    vec.append(vec_i)
output = []
for line in vec:
    a = set(find_divisor(line[0]))
    b = set(find_divisor(line[1]))
    co_div = list(a&b)
    co_div.sort()
    m_co_div = co_div.pop()
    output.append(int(m_co_div*(line[0]/m_co_div)*(line[1]/m_co_div)))
for i in output:
    print(i)