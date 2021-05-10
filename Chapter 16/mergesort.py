from stack import Stack

def pop(stack, n):
    vals = []
    for _ in range(n):
        vals.append(stack.pop())
    vals.reverse()
    return vals

def push(stack, *args):
    for arg in args:
        stack.push(arg)

def merge(eval_stack, call_stack):
    x, y = pop(eval_stack, 2)

    i, n = 0, len(x)
    j, m = 0, len(y)
    z = []
    while i < n and j < m:
        if x[i] <= y[j]:
            z.append(x[i])
            i += 1
        else:
            z.append(y[j])
            j += 1
    if i < n:
        assert j == m
        z.extend(x[i:])
    if j < m:
        assert i == n
        z.extend(y[j:])

    push(eval_stack, z)

def merge_sort(x):
    eval_stack = Stack()
    call_stack = Stack()

    # First function call: merge_sort_rec(x, 0, len(x))
    push(eval_stack, x, 0, len(x))
    call_stack.push(merge_sort_rec)
    
	# Handle all function calls until we are done
    while call_stack:
        call = call_stack.pop()
        call(eval_stack, call_stack)
    return eval_stack.pop()

def merge_sort_rec(eval_stack, call_stack):
    x, low, high = pop(eval_stack, 3)

    if high - low <= 1:
        eval_stack.push(x[low:high])
    else:
        mid = (low + high) // 2

        #right = merge_sort_rec(x, mid, high)
        push(eval_stack, x, mid, high)
        call_stack.push(merge_sort_right)

        #left = merge_sort_rec(x, low, mid)
        push(eval_stack, x, low, mid)
        call_stack.push(merge_sort_rec)

def merge_sort_right(eval_stack, call_stack):
    x, low, high, left = pop(eval_stack, 4)

    # save left for merge but call merge sort
    # with the interval
    push(eval_stack, left, x, low, high)

    # first call recursively, then merge
    call_stack.push(merge)
    call_stack.push(merge_sort_rec)

x = [1, 6, 2, 4, 7]
print(merge_sort(x))
