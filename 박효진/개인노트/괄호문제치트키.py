
judge_data = input()
stack = []
for i in judge_data:
    if i == "{" or i == "(" or i == '[':            # 좌측 괄호 데이터를 받으면 조건에 상관 없이 stack에 push
        stack.append(i)                             # 괄호에 조건을 확인하여 짝이 맞다면 해당 요소 pop.
    elif stack and i == "}" and stack[-1] == "{":   # stack이 비어있지 않고, top의 요소와 짝이 맞는지 확인  
        stack.pop()
    elif stack and i == ")" and stack[-1] == "(":   # stack이 비어있지 않고, top의 요소와 짝이 맞는지 확인 
        stack.pop()
    elif stack and i == "]" and stack[-1] == "[":   # stack이 비어있지 않고, top의 요소와 짝이 맞는지 확인
        stack.pop()
    elif i == "}" or i == ")" or i == ']':          # 만약 stack이 비어있고 i가 닫힌 괄호일때도 push한다 
                                                    # 또한 괄호의 순서가 잘못되어도 stack에 쌓이게 되는 것을 볼 수 있다.
        stack.append(i)                             # 잘못된 식인것을 출력하기 위함이며 
                                                    # 짝이 맞지 않기 때문에 스택에 끝까지 남아있는다.
if stack:
    answer = 'Fail'                                 # 스택에 데이터가 남아있다면 짝이 맞지 않다는 뜻이므로 Fail
else:
    answer = 'Success'                              # 문제가 없다면 Success

print(answer)
