T = int(input())
 
for tc in range(1, T+1):
    s = input()
    stack = []
    for i in s:
        if i == "{" or i == "(" or i == '[':
            stack.append(i)
        elif stack and i == "}" and stack[-1] == "{":
            stack.pop()
        elif stack and i == ")" and stack[-1] == "(":
            stack.pop()
        elif stack and i == "]" and stack[-1] == "[":
            stack.pop()
        elif i == "}" or i == ")" or i == ']':
            stack.append(i)
 
    if stack:
        answer = 0
    else:
        answer = 1
 
    print(f"#{tc}", answer)