from stack import Stack

opening = "({["
closing = ")}]"


def check_balanced(string: str) -> str:
    stack: Stack = Stack()
    index: int = 0
    balance: bool = True
    while index < len(string):
        if string[index] in opening:
            stack.push(string[index])
        elif string[index] in closing:
            if stack.is_empty():
                balance = False
            elif closing.find(string[index]) == opening.find(stack.peek()):
                stack.pop()
            else:
                balance = False
        index += 1
    if stack.is_empty() and balance:
        return "Строка сбалансирована"
    else:
        return "Строка не сбалансирована"
