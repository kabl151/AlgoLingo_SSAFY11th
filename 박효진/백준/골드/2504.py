import sys
input = sys.stdin.readline

wd = input()
stack = []
try:
    for i in wd:
        if i == '(' or i == '[':
            stack.append(i)
        elif len(stack) == 0 and (i == ')' or i == ']'):
            stack.append(i)
        elif len(stack) != 0 and i == ')' and stack[-1] == '[':
            stack.append(i)
        elif len(stack) != 0 and i == ']' and stack[-1] == '(':
            stack.append(i)
        elif len(stack) != 0 and i == ')' and stack[-1] == '(':
            stack.pop()
            stack.append(str(2))
        elif len(stack) != 0 and i == ']' and stack[-1] == '[':
            stack.pop()
            stack.append(str(3))
        elif len(stack) != 0 and i == ')' and stack[-1].isdigit():
            if stack[-2] == '(':
                a = int(stack.pop())
                stack.pop()
                stack.append(str(int(a)*2))
                while True:
                    if len(stack) > 1 and stack[-2].isdigit():
                        a = int(stack.pop())
                        b = int(stack.pop())
                        stack.append(str(a + b))
                    else:
                        break
            elif stack[-2].isdigit():
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(str(a + b))
                while True:
                    if len(stack) > 1 and stack[-2].isdigit():
                        a = int(stack.pop())
                        b = int(stack.pop())
                        stack.append(str(a + b))
                    else:
                        break
            else:
                stack.append(i)
        elif len(stack) != 0 and i == ']' and stack[-1].isdigit():
            if stack[-2] == '[':
                a = int(stack.pop())
                stack.pop()
                stack.append(str(int(a)*3))

                while True:
                    if len(stack) > 1 and stack[-2].isdigit():
                        a = int(stack.pop())
                        b = int(stack.pop())
                        stack.append(str(a + b))
                    else:
                        break

            elif stack[-2].isdigit():
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(str(a + b))
                while True:
                    if len(stack) > 1 and stack[-2].isdigit():
                        a = int(stack.pop())
                        b = int(stack.pop())
                        stack.append(str(a + b))
                    else:
                        break
            else:
                stack.append(i)

        if len(stack) > 1:
            if stack[-1].isdigit() and stack[-2].isdigit():
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(str(a + b))

    if '(' in stack or '[' in stack or ')' in stack or ']' in stack:
        print(0)
    else:
        print(*stack)
except Exception:
    print(0)