count = int(input())
test_case = []
for i in range(count*2):
    test_case.append(input())
index = 0
while True:
    hamming = 0
    if (index >= count*2):
        break
    for i in range(len(test_case[index])):
        if test_case[index][i] != test_case[index+1][i]:
            hamming += 1
    print(f"Hamming distance is {hamming}.")
    index += 2