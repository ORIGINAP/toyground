opr_lst=["+","-","*","/"]
def define_opr(pre,post):
    pre_fix = pre.copy()
    post_cp = post.copy()
    if(len(post)>0):
        for i in post:
            pre_fix.append(post.pop(i))
            define_opr(pre_fix, post)
    else:
        print(pre_fix)

for i in range(3,-1,-1):
    post_opr = opr_lst.copy()
    post_opr.remove(opr_lst[i])
    pre_fix = [opr_lst[i]]
    define_opr(pre_fix,post_opr)

print("hello")