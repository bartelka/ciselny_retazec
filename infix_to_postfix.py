class Stack:
    def __init__(self):
        self.values = []

    def is_empty(self):
        if len(self.values) == 0:
            return True
        else:
            return False

    def push(self, value):
        self.values.append(value)

    def pop(self):
        if not self.is_empty():
            return self.values.pop()
        else:
            return IndexError("zasobnik je prazdny")

def precedence(op):
    if op in ['+', '-']:
        return 1
    if op in ['*', '/']:
        return 2
    return 0

def infix_to_postfix(vyraz):
    op_stack = Stack()
    output_list = []
    for i in vyraz:
        if i in "0123456789":
            output_list.append(i)
        elif i == '(':
            op_stack.push(i)
        elif i == ')':
            while not op_stack.is_empty() and op_stack.values[-1] != '(':
                output_list.append(op_stack.pop())
            op_stack.pop()
        else:
            while (not op_stack.is_empty() and op_stack.values[-1] != '(' and
                   precedence(op_stack.values[-1]) >= precedence(i)):
                output_list.append(op_stack.pop())
            op_stack.push(i)
    while not op_stack.is_empty():
        output_list.append(op_stack.pop())
    return output_list

def vypis(zoznam):
    return "".join(zoznam)

vyraz = input("Zadaj výraz: ")
print(vypis(infix_to_postfix(vyraz)))

#vyraz
# (9+(3*6)/(8-3))
