chess_list = [1,1,2,2,2,8]
input_chess = list(map(int,input().split()))
calc_rslt = list(map(lambda x,y:x-y,chess_list,input_chess))
calc_rslt = list(map(str,calc_rslt))
print(" ".join(calc_rslt))