from string import ascii_uppercase
a_list = list(ascii_uppercase)
count = int(input())
val = []
for i in range(count):
    val_i = input()
    val_d = list(dict.fromkeys(list(val_i),0))
    val.append("".join(val_d))
a_sum = 0
for i in range(65,91):
    a_sum += i
a_list = map(str,a_list)
a_list = "".join(a_list)
for word in val:
    o_sum = 0
    for c in word:
        o_sum += ord(a_list[a_list.find(c)])
    print(a_sum - o_sum)