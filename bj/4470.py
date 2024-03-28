count = int(input())
str = []
for i in range(count):
    str_i = input()
    str.append(str_i)
for i in range(count):
    print(f"{i+1}. {str[i]}")