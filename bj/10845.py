import sys
count = int(sys.stdin.readline())
order = []
for i in range(count):
    order.append(sys.stdin.readline().split())
_que = []
def _push(x):
    _que.append(x)
def _pop():
    if _que != []:
        p_out = _que.pop(0)
    else: p_out = -1
    print(p_out)
    return p_out
def _size():
    print(len(_que))
def _empty():
    if len(_que) > 0: print("0")
    else: print('1')
def _front():
    try:
        print(_que[0])
    except:
        print('-1')
def _back():
    try:
        temp = _que.pop()
        print(temp)
        _que.append(temp)
    except:
        print(-1)
def stack_kiosk(_order):
    if _order[0] == "push": 
        v = _order[1]
        _push(int(v))
    elif _order[0] == "pop": _pop()
    elif _order[0] == "size": _size()
    elif _order[0] == "empty": _empty()
    elif _order[0] == "front": _front()
    elif _order[0] == "back": _back()
for i in range(count):
    stack_kiosk(order[i])