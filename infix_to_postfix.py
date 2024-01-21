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
    vyraz = [i for i in vyraz if i != " "]
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

def stack_processing(vyraz):
    operand_stack = Stack()
    o_list = [i for i in vyraz]
    for i in o_list:
        if i in "0123456789":
            operand_stack.push(int(i))
        if i in "+-*/":
            operand_2 = operand_stack.pop()
            operand_1 = operand_stack.pop()
            op = vypocet(i, operand_1, operand_2)
            operand_stack.push(op)
    return operand_stack.pop()

def vypocet(operator:str, operand_1:int, operand_2:int):
    if operator == "+":
        return operand_1 + operand_2
    if operator == "-":
        return operand_1 - operand_2
    if operator == "*":
        return operand_1 * operand_2
    if operator == "/":
        return operand_1 / operand_2


vyraz = input("Zadaj výraz: ")
print(vypis(infix_to_postfix(vyraz)))
print(stack_processing(vypis(infix_to_postfix(vyraz))))

#vyraz
# ( 9 + ( 3 * 6 ) / ( 8 - 3 ) )
