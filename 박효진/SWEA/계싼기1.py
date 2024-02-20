# 중복으로 문제를 올리신 이유가 아마 직접 구현해보라는 의미인 것 같아 중위 > 후위 > 후위계산으로 진행했습니다.
T = 10
for tc in range(1, T+1):
    n = int(input())
    wd = input()
    stack = []
    result = ''
    for i in wd:
        if i.isdigit():
            result += i
        else:
            if len(stack) == 0 or stack[-1] != '+':
                stack += i
            elif len(stack) != 0 and stack[-1] == '+':
                result += stack.pop()
                stack += i
    result += stack.pop()   # 후위 계산식 작성 완료. 
    # 작성된 후위 계산식을 다시 계산
    stack_2 = []
    for j in result:
        if j.isdigit():
            stack_2.append(int(j))
        else:
            b = stack_2.pop()
            a = stack_2.pop()
            stack_2.append(a+b)
    print(f'#{tc}', *stack_2)
