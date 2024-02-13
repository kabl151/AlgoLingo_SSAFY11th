text = '(1+(1+3)*4/5)'
# 스택을 사용한 후위식으로 표현 바꾸기
stack = [] # append(x) / pop()
result = '' # 후위식을 넣을 result 변수 설정
# 스택의 상태가 항상 내가 넣으려고 하는 연산자가
# 기존에 있었던 연산자보다 우선순위가 높도록 유지
# 중위식을 순회하면서 후위식을 만들어야한다.

for ch in text:
    # 1. 숫자가 나오면 그대로 출력
    if ch.isdigit():
        result += ch
    # 2. '(' 여는 괄호가 나오면
    elif ch == '(':
        # ( 여는 괄호를 스택에 push한다
        stack.append(ch)
    # 3. '*' '/' 나오면
    elif ch == '*' or ch == '/':
        # 스택에 들어있는 값이 * or / 연산자라면
        # 들어있던 연산자를 먼저 빼준다
        if len(stack) > 0 and (stack[-1] == '*' or stack[-1] == '/'):
            result += stack.pop()
        stack.append(ch)

    # 4. '+' '-' 나오면
    elif ch == '+' or ch == '-':
        # 스택내에 나보다 높은 우선순위가 바로 아래에 없게끔 만들어야 한다.
        # 우선순위가 나보다 아래인 경우를 먼저보면 스택이 비어있거나 여는괄호가있다면 그냥 append
        # 위의 조건을 만족하기 위해 여는 괄호가 나오거나 스택이 아에 비울때까지 pop을 반복 먼저해야한다
        while len(stack) > 0 and stack[-1] != '(':
            result += stack.pop()
        stack.append(ch)
    # 5. ')' 닫는 괄호가 나오면
    elif ch == ')':
        # '(' 여는 괄확 나올 때까지 pop해라
        while stack[-1] != '(':
            result += stack.pop()
        stack.pop()     # while 다 돌고 '(' 까지 제거해준다
# 순회가 끝난 후, stack의 내용을 모두 pop 해준다.
while len(stack) > 0:
    result += stack.pop()

print(result)


# 후위에서 중위로 바꾸는것 = > 계산기 2 문제.
text = '113+4*5/+'
stack = []
for ch in text:
    # 피연산자를 스택에 넣고
    if ch.isdigit():
        stack.append(ch)
    # 연산자를 만나면 피연산자를 두개 빼서 연산한다. 그 결과를 다시 스택에 넣는다.
    else:   # 피연산자 제외한 연산자 모두
        b = int(stack.pop())
        a = int(stack.pop())
        if ch == '*':
            stack.append(a*b)
        elif ch == '/':
            stack.append(a//b)
        elif ch == '+':
            stack.append(a+b)
        elif ch == '-':
            stack.append(a-b)
    # 순회가 다 돌고나면 stack에는 결과만 남게된다
result = stack.pop()
print(result)


# ------------------------------------ 우선순위에 대한 딕셔너리를 통한 구현

text = '(1+(1+3)*4/5)'

stack = [] 
result = ''

icp = {'*' : 2, 
       '/' : 2, 
       '+' : 1,
       '-' : 1,
       '(' : 3} # 입력될 때의 연산자 우선순위
isp = {'*' : 2, 
       '/' : 2, 
       '+' : 1,
       '-' : 1,
       '(' : 0} # 스택 내에 있을 때의 연산자 우선순위
for ch in text:
    # 1. 숫자(피연산자)가 나오면 그대로 출력
    if ch.isdigit():
        result += ch
    # 2. 연산자 * / + - ( 포함이 된다면
    if ch in ['*','/','+','-','(']:
        # - 입력된 연산자가 > 스택 맨 위의 연산자보다 우선순위
        if len(stack) == 0 or icp[ch] > isp[stack[-1]]:
            stack.append(ch)
        # - 입력된 연산자가 <= 스택 맨 위의 연산자보다 우선순위
        else:
            while len(stack) > 0 and icp[ch] <= isp[stack[-1]]:
                result += stack.pop()
            stack.append(ch)
    elif ch == ')':
        # '(' 여는 괄확 나올 때까지 pop해라
        while stack[-1] != '(':
            result += stack.pop()
        stack.pop()     # while 다 돌고 '(' 까지 제거해준다
# 순회가 끝난 후, stack의 내용을 모두 pop 해준다.
while len(stack) > 0:
    result += stack.pop()

print(result)            

# 연산자들을 딕셔너리에 람다식을 통해 간결하게 표현 가능
text = '(1+(1+3)*4/5)'
oper = { # 연산자 - 람다식을 key-value로 매칭
    '*' : lambda a, b : a * b,
    '/' : lambda a, b : a // b,
    '+' : lambda a, b : a + b,
    '-' : lambda a, b : a - b
}
stack = []
for ch in text:
    # 피연산자를 스택에 넣고
    if ch.isdigit():
        stack.append(ch)
    # 연산자를 만나면 피연산자를 두개 빼서 연산한다. 그 결과를 다시 스택에 넣는다.
    else:   # 피연산자 제외한 연산자 모두
        b = int(stack.pop())
        a = int(stack.pop())
        temp = oper[ch](a,b)
        stack.append(temp)
    # 순회가 다 돌고나면 stack에는 결과만 남게된다
result = stack.pop()
print(result)