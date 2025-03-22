num_set=[1,2,3,4,5]
opr_lst=["+","/","-","*"]
wordset = ['','','','']
depth = 0
result = []
opr_len = len(opr_lst)

def select_opr(opr_lst,wordset,depth,result):
    if(depth<opr_len):
        for i in opr_lst:
            opr_lst_cp=opr_lst.copy()
            wordset[depth] = i
            opr_lst_cp.remove(i)
            select_opr(opr_lst_cp,wordset,depth+1,result)
    else:
        result += wordset
        
select_opr(opr_lst,wordset,depth,result)
result = [result[i:i+4] for i in range(0,len(result),4)]
print(result)
print(len(result))