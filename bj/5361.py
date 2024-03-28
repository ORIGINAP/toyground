import sys
menu = [350.34, 230.90, 190.55, 125.30, 180.90]
input = sys.stdin.readline
count = int(input())
order = []
for i in range(count):
    order_i = list(map(float, input().split()))
    order.append(order_i)
_sum = []
result = 0.0
for i in order:
    for j in range(len(i)):
        result += (float(i[j])*menu[j])
    _sum.append(result)
for c in _sum:
    print(f"{c:.2f}")
                