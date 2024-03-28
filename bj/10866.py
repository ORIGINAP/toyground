import sys
count = int(sys.stdin.readline())
order = []
for i in range(count):
    order.append(sys.stdin.readline().split())
_deque = []
def _push_back(x):
    _deque.append(x)
def _push_front(x):
    if _deque == []:
        _deque.append(x)
    else:
        _deque.reverse()
        _deque.append(x)
        _deque.reverse()
def _pop_front():
    if _deque != []:
        p_out = _deque.pop(0)
    else: p_out = -1
    print(p_out)
def _pop_back():
    if _deque != []:
        p_out = _deque.pop()
    else: p_out = -1
    print(p_out)
def _size():
    print(len(_deque))
def _empty():
    if len(_deque) > 0: print("0")
    else: print('1')
def _front():
    try:
        print(_deque[0])
    except:
        print('-1')
def _back():
    try:
        temp = _deque.pop()
        print(temp)
        _deque.append(temp)
    except:
        print(-1)
def stack_kiosk(_order):
    if _order[0] == "push_back": 
        v = _order[1]
        _push_back(int(v))
    elif _order[0] == "push_front": 
        v = _order[1]
        _push_front(int(v))
    elif _order[0] == "pop_front": _pop_front()
    elif _order[0] == "pop_back": _pop_back()
    elif _order[0] == "size": _size()
    elif _order[0] == "empty": _empty()
    elif _order[0] == "front": _front()
    elif _order[0] == "back": _back()
for i in range(count):
    stack_kiosk(order[i])