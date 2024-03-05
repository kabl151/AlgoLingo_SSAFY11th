
def push(data, size):
    global top
    top += 1
    if top == size:
        print('overflow')
    else:
        stack[top] = data

def pop(stack,top):
    if len(stack) == 0:
        # underflow : 리스트가 비어있을때 오류를 피하기 위함
        return
    else:
        top -= 1
        stack.append(0)         # 스택 size 유지
        return stack.pop(top+1) # + 1은 인덱스 보정
    
size = 10               # 스택 사이즈
stack = [0] * size      # 파이썬에서는 최적화가 아닌이상 필요한 부분은 아님
top = -1                # top의 초기 위치

push('A', size)         # data와 size를 인자로 넣어준다
top += 1                # 스택에 데이터가 쌓일때마다 마지막 삽입된 데이터 위치 증가
stack[top] = 'B'        # push('B')
push('C', size)

pop(stack,top)          # top에 있는 데이터 삭제

print(stack)            # ['A', 'B', 0, 0, 0, 0, 0, 0, 0, 0]
print(top)              # top의 위치 2

def push(data, stack):              # 가변형인 리스트에서는 push로 인한 overflow 조건은 필요없다
    stack.append(data)              # 데이터를 자동으로 스택의 top 부분에 추가
    return print(stack)             # 스택 출력(보기위함)

def pop(stack):
    if len(stack) == 0:             # 비어있는데 pop을 했을경우 오류 발생하므로 조건 추가
        return print('underflow')
    else:
        return print(stack.pop())   # 스택의 top부분을 삭제
    
stack = []
                # push된 데이터 출력
push(1, stack)  # [1]
push(2, stack)  # [1, 2]
push(3, stack)  # [1, 2, 3]

                # pop된 데이터 출력
pop(stack)      # 3
print(stack)    # [1, 2]

pop(stack)      # 2
print(stack)    # [1]

pop(stack)      # 1
print(stack)    # []