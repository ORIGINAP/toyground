#문제 요구사항
#연산자 + - * / 가 0 0 0 0 자리에 따라 갯수로 주어진다.
#첫줄에 숫자의 갯수가 주어진다.
#연산자는 숫자-1개 만큼 주어진다.
#연산자의 계산 순서는 앞에서 부터 계산한다.(기존 연산 법칙을 무시한다.)
#주어진 연산자로 만들 수 있는 모든 경우의 수를 계산한다.
#첫줄에 최댓값, 그 다음줄에 최솟값을 출력한다.

'''
개선사항 : 중복계산(중복을 잡지 않는 순열)
방문여부 탐색? dfs
'''

import sys
input = sys.stdin.readline
l = int(input())
num_set = list(map(int,input().split()))
opr_count = list(map(int,input().split()))

opr_lst = []
opr_len = 0

opr_lst = ["+"] * opr_count[0] + ["-"] * opr_count[1] + ["*"] * opr_count[2] + ["/"] * opr_count[3]
opr_len = len(opr_lst)

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

def make_output(opr_lst, pre_result,  )