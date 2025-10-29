numsize = int(input())
numlist = list(map(int,input().split()))
opr = list(map(int,input().split()))

opr_set = []
opr_mat = []
count = 0
check = []
for c in opr:
	count += 1
	for i in range(0,c):
		opr_set.append(count)
def makeMatrix():
	for i in opr_set:
	    check.append(0)
	    opr_mat.append(opr_set)
makeMatrix()
row = 0
min_max_list = []
def calcurate(p1, p2, opr):
    if(opr == 1):
        return p1+p2
    if(opr == 2):
        return p1-p2
    if(opr == 3):
        return p1*p2
    if(opr == 4):
        if(p1 < 0 and p2 > 0):
            p1 = p1*-1
            return -(p1//p2)
        elif(p2 > 0 and p2 < 0):
            p2 = p2*-1
            return -(p1//p2)
        else:
            return p1//p2

def backTracking(row, sum, progress):
    if(row == numsize-1):
        min_max_list.append(sum)
        return
    for i in range(0, numsize-1):
        if(check[i]==0):
            check[i] = 1
            backTracking(row+1,calcurate(sum,numlist[progress+1],opr_mat[row][i]),progress+1)
            check[i] = 0
backTracking(0,numlist[0],0)
print(max(min_max_list))
print(min(min_max_list))
#count 1: + 2: - 3: x 4: 