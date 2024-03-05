T = 10
for tc in range(1, T + 1):
    N = int(input())
    st = input()
    stack = []
    result = []
    for i in st:
        if i.isdigit():
            result.append(i)
        elif len(stack) == 0 and (i == '+' or i =='*'):
            stack.append(i)
        elif len(stack) != 0 and (i == '+' or i =='*'):
            if i == '+' and stack[-1] == '+':
                result.append(stack.pop())
                stack.append(i)
            elif i == '+' and stack[-1] == '*':
                result.append(stack.pop())
                if len(stack) != 0:
                    result.append(stack.pop())
                    stack.append(i)
                else:
                    pass
            elif i == '*' and stack[-1] == '+':
                stack.append(i)
            elif i == '*' and stack[-1] == '*':
                result.append(stack.pop())
                stack.append(i)
    for j in range(len(stack)):
        result.append(stack.pop())
    # print(*result, sep = '')
    new_result = []
    for k in result:
        if k.isdigit():
            new_result.append(k)
        else:
            b = new_result.pop()
            a = new_result.pop()
            if k =='+':
                new_result.append(int(a)+int(b))
            elif k =='*':
                new_result.append(int(a)*int(b))
    print(f'#{tc}', sum(new_result))