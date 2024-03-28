count = int(input())
vec = []
for i in range(count):
    x_i, y_i = map(int,input().split())
    vec.append([x_i,y_i])
vec_sort = sorted(vec, key = lambda x:(x[0],x[1]), reverse=True)
progress = 1
score = 1
output = []
print(vec_sort)
for i in range(count):
    if i > 0:
        if vec_sort[i-1][1] >= vec_sort[i][1]:
            if score < progress: score = progress
            output.append(score)
            if i > 1:
                score += 1
            print(f'1 - i = {i}, score = {score} progress = {progress}')
        elif vec_sort[i-1][1] < vec_sort[i][1]:
            print(f'2 - i = {i}, score = {score} progress = {progress}')
            output.append(score)
    elif i == 0:
        output.append(score)
    progress += 1
print(output)