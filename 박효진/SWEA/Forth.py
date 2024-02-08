T = int(input())
for tc in range(1, T + 1):
    lst = list(map(str, input().split()))
    stack = []
    num_lst = []
    oper_lst = []
    for i in lst:
        if i != '+' and i != '-' and i != '/' and i != '*' and i != '.':
            num_lst.append(int(i))
        elif i == '.':
            continue
        else:
            oper_lst.append(i)
    if len(num_lst) == len(oper_lst)+1:
        for i in lst:
            if i != '+' and i != '-' and i != '/' and i != '*' and i != '.':
                stack.append(int(i))
            elif i == '+':
                stack_2 = stack.pop(-1)
                stack_1 = stack.pop(-1)
                result = stack_1 + stack_2
                stack.append(result)
            elif i == '-':
                stack_2 = stack.pop(-1)
                stack_1 = stack.pop(-1)
                result = stack_1 - stack_2
                stack.append(result)
            elif i == '/':
                stack_2 = stack.pop(-1)
                stack_1 = stack.pop(-1)
                result = stack_1 // stack_2
                stack.append(result)
            elif i == '*':
                stack_2 = stack.pop(-1)
                stack_1 = stack.pop(-1)
                result = stack_1 * stack_2
                stack.append(result)
            elif i == '.':
                break
        print(f'#{tc}', *stack)
    else:
        print(f'#{tc} error')