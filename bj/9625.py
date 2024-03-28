import sys
input = sys.stdin.readline
count = int(input())
ab_list = [0,1]
for i in range(count-1):
    tem_a,tem_b = [ab_list[0],ab_list[1]]
    ab_list[0] = tem_b
    ab_list[1] = tem_a+tem_b
print(ab_list[0],ab_list[1])