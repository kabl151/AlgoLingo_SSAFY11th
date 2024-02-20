wd = input()
stack = []
result = ''
for i in wd:
    if i != '+' and i != '-' and i != '/' and i != '*' and i != '(' and i != ')':
        result += i
    elif i == '(':
        stack.append(i)
    elif (i == '+' or i == '-') and (len(stack) == 0 or stack[-1] == '('):
        stack.append(i)
    elif (i == '+' or i == '-') and len(stack) != 0:
        if stack[-1] == '+' or stack[-1] == '-':
            pop_wd = stack.pop()
            stack.append(i)
            result += pop_wd
        else:
            result += i
    elif (i == '/' or i == '*') and (len(stack) == 0 or stack[-1] == '('):
        stack.append(i)
    elif (i == '/' or i == '*') and len(stack) != 0:
        if stack[-1] == '*' or stack[-1] == '/':
            pop_wd = stack.pop()
            stack.append(i)
            result += pop_wd            
        else:
            stack.append(i)
    elif i == ')':
        while True:
            pop_wd = stack.pop()
            if pop_wd == '(':
                break
            result += pop_wd
pop_wd = stack.pop()
result += pop_wd
print(result)


