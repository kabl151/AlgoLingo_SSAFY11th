T = int(input())
for tc in range(1, T+1):
    problem = list(input())
    cnt = 0
    memory = 0
    for i in range(len(problem)):
        if problem[i] == '0':
            continue
        elif problem[i] == '1':
            cnt += 1
            for j in range(i, len(problem)):
                if problem[j] == '1':
                    problem[j] = '0'
                else:
                    problem[j] = '1'
    print(f'#{tc}', cnt)