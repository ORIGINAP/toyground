import sys
count = int(sys.stdin.readline())
order = []
for i in range(count):
    order.append(sys.stdin.readline().split())
_stack = []
def _push(x):
    _stack.append(x)
def _pop():
    if _stack != []:
        p_out = _stack.pop()
    else: p_out = -1
    print(p_out)
    return p_out
def _size():
    print(len(_stack))
def _empty():
    if len(_stack) > 0: print("0")
    else: print('1')
def _top():
    temp = _pop()
    if temp != -1:
        _stack.append(temp)
def stack_kiosk(_order):
    if _order[0] == "push": 
        v = _order[1]
        _push(int(v))
    elif _order[0] == "pop": _pop()
    elif _order[0] == "size": _size()
    elif _order[0] == "empty": _empty()
    elif _order[0] == "top": _top()
for i in range(count):
    stack_kiosk(order[i])