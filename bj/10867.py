import sys
size = sys.stdin.readline()
num = sys.stdin.readline().strip().split()
num = list(map(int,num))
num = list(dict.fromkeys(num))
num.sort()
num = list(map(str,num))
print(" ".join(num).strip())