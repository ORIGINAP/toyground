from collections import Counter
word = input().lower()
count_list = sorted(Counter(word).items(), key = lambda x : x[1], reverse=True)
if len(count_list) == 1: print(count_list[0][0].upper())
elif count_list[0][1] == count_list[1][1] : print("?")
else : print(count_list[0][0].upper())