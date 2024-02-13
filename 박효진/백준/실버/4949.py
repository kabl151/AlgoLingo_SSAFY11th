while True:
    wd = input()
    stack_lst = []
    if wd == '.':
        break
    else:
        wd = wd.strip()
        for i in wd:
            if i == '[' or i == '(':
                stack_lst.append(i)
            elif len(stack_lst) != 0 and i == ']' and stack_lst[-1] == '[':
                stack_lst.pop()
            elif len(stack_lst) != 0 and i == ')' and stack_lst[-1] == '(':
                stack_lst.pop()
            elif i == ']' or i == ')':
                stack_lst.append(i)
            elif '.' == i:
                break
        if len(stack_lst) == 0:
            print('yes')
        else:
            print('no')