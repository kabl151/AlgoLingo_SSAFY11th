# 스택이라는 기본 자료형의 자료구조 (파이썬에서는 리스트)
stack = []
# 스택에 필요한 연산... (뒤에서부터 삽입 / 뒤에서부터 삭제)
def push(x): # x를 삽입
    stack.append(x)

def pop():# 마지막 요소를 빼내고 반환
    # 리스트가 비어있다면 오류가 날 수 있기 때문에 예외처리 필요
    if len(stack) == 0: # len(stack) 대신 그냥 stack: 해도 됨.
        return
    return stack.pop()

def peak(): # 마지막 요소의 값을 반환
    if len(stack) == 0:
        return
    return stack[-1]

# 스택에 1, 2, 3 이라는 값을 순서대로 넣고,
# 해당 값을 3번 빼내어 출력!

push(1)
push(2)
push(3)
item = pop()
print(item)     # 3
item = pop()
print(item)     # 2
item = pop()
print(item)     # 1


