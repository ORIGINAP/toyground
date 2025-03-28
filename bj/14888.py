import sys
input = sys.stdin.readline
l = int(input())
num_set = list(map(int,input().split()))
opr_count = list(map(int,input().split()))

opr_lst = []
opr_len = 0

opr_lst = ["+"] * opr_count[0] + ["-"] * opr_count[1] + ["*"] * opr_count[2] + ["/"] * opr_count[3]
opr_len = len(opr_lst)
     
wordset = []
depth = 0
result = []

def calc(a,opr,b):
    if(opr=='+'):
        return a+b
    elif(opr=='-'):
        return a-b
    elif(opr=='*'):
        return a*b
    elif(opr=='/'):
        if(a*b<0):
            return -(abs(a)//abs(b))
        return a//b

def select_opr(opr_lst,wordset,depth,output):
    if(depth<opr_len):
        for i in range(0,len(opr_lst)):
            opr_lst_cp=opr_lst.copy()
            wordset.append(opr_lst[i])
            opr_lst_cp.pop(i)
            select_opr(opr_lst_cp,wordset,depth+1,output)
            wordset.pop()
    else:
        output+=wordset

def include_opr(num_set, wordset, result,n):
    if(n+1<len(num_set)):
        res = calc(result,wordset[n],num_set[n+1])
        result = include_opr(num_set, wordset, res, n+1)
    return result

def mix_max(sum):
    print(max(sum))
    print(min(sum))

select_opr(opr_lst,wordset,depth,result)
result = [result[i:i+opr_len] for i in range(0,len(result),opr_len)]
sum = []
for n in range(0,len(result)):
    sum.append(include_opr(num_set,result[n],num_set[0],0))
mix_max(sum)
