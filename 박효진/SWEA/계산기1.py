T = 10
for tc in range(1, T + 1):
    N = int(input())
    wd = input()
    stack = []
    dct = {
        '0' : 0,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9
    }
    for i in wd:
        if i != '+':
            value = dct[i]
            stack.append(value)
        else:
            pass
    print(f'#{tc} {sum(stack)}')