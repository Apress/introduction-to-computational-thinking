from stack import Stack

class MalformedExpression(Exception):
    pass

def calc(*expressions):
    try:
        eval_stack = Stack()
        for expr in expressions:
            if expr in ops:
                ops[expr](eval_stack)
            else:
                eval_stack.push(expr)
        result = eval_stack.pop()
    except EmptyStack:
        raise MalformedExpression()

    if not eval_stack.is_empty():
        raise MalformedExpression()
    return result

def add(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a + b)

def sub(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a - b)

def mul(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a * b)

def div(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a / b)

def unary_minus(stack):
    a = stack.pop()
    stack.push(-a)

ops = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '~': unary_minus
}

print(calc(2, 3, '+', 2, '*', '~'))
