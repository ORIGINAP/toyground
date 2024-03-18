count = int(input())
case=[]
case_s=[]
for i in range(count):
    case_i, case_s_i = input().split()
    case.append(case_i)
    case_s.append(case_s_i)
p_case = []
for i in range(count):
    temp = ""
    for j in case_s[i]:
       temp +=j*int(case[i])
    p_case.append(temp)
for i in range(count):
    print(p_case[i])
    