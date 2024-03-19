val = []
while(1):
    val_i = input()
    if(val_i == "0 0"):
        break
    else:
        val.append(val_i)

for i in val:
    div, div2 = map(int,i.split())
    print(div+div2)