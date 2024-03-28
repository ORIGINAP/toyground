count = int(input())
vec = []
for i in range(count):
    x_i, y_i = map(int,input().split())
    vec.append([x_i,y_i])
score_list = []
for obj in vec:
    score = 1
    for i in range(count):
        if obj[0] < vec[i][0] or obj[1] < vec[i][1]:
            score +=1
            if obj[0] >= vec[i][0] or obj[1] >= vec[i][1]:
                score -=1
    score_list.append(score)
score_list = map(str,score_list)
print(" ".join(score_list))