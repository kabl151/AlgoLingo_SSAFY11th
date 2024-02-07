# 열리면 한개씩 추가
# 레이져 쏘면 쌓인 갯수만큼 배수
# 닫힐때도 카운트 but 한개씩 뺴기
# 다시 열리면 다시 추가
# 쐈을때 남아있는 막대만큼 더해준다.

# cnt = 0
# 0*1 + + + 3*1 3*1 - + 3*1 - 2*1 - - + 1* -

# T = int(input())
# for tc in range(1,T+1):
stack = []
lazer = list(input())
cnt = 0

for lz in lazer:
    if lz == '(' and (len(stack) == 0 or stack[-1] != ')'):
        stack.append(lz)
    elif lz == '(' and stack[-1] == '(':
        stack.append(lz)
    elif lz == ')' and stack[-1] == ')':
        stack.pop()
    elif lz == ')' and stack[-1] == '(':
        stack.pop()
        cnt += len(stack)
print(cnt)