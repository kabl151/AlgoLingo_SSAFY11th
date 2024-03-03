# import sys
# sys.stdin = open('input (2).txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    barcode = [list(map(int, input())) for _ in range(N)]
    stack = ''
    result = []
    dct = {'0001101': 0,
           '0011001': 1,
           '0010011': 2,
           '0111101': 3,
           '0100011': 4,
           '0110001': 5,
           '0101111': 6,
           '0111011': 7,
           '0110111': 8,
           '0001011': 9}
    for i in range(N):
        for j in range(1, M+1):
            now = barcode[i][-j]
            if now == 1:
                for k in range(56):
                    stack += str(barcode[i][-j-k])
                break
        if len(stack) > 0:
            break
    stack = stack[::-1]
    for i in range(0,56,7):
        code = stack[i:i+7]
        num = dct[code]
        result.append(num)
    final_num = sum(result[::2]) * 3 + sum(result[1::2])
    if final_num % 10 == 0:
        print(f'#{tc}',sum(result))
    else:
        print(f'#{tc}',0)