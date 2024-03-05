T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for _ in range(M):
        pos, num, oper = map(int, input().split())
        # 행동 1일때
        if oper == 1:
            idx = pos - 1
            for i in range(num):
                if arr[idx] == 0:
                    arr[idx] = 1
                else:
                    arr[idx] = 0
                idx += 1
                if idx > len(arr) - 1:
                    break
        # 행동 2일때
        elif oper == 2:
            idx = pos - 1
            color = arr[idx]
            for i in range(num-1):
                if arr[idx + 1] != color:
                    arr[idx + 1] = color
                idx += 1
                if idx + 1 > len(arr) - 1:
                    break
        # 행동 3일때
        elif oper == 3:
            idx = pos - 1
            idx_left = idx - 1
            idx_right = idx + 1
            for i in range(num):
                if arr[idx_left] == arr[idx_right]:
                    if arr[idx_left] == 0:
                        arr[idx_left] = 1
                        arr[idx_right] = 1
                    else:
                        arr[idx_left] = 0
                        arr[idx_right] = 0
                idx_left -= 1
                idx_right += 1
                if idx_left < 0 or idx_right > len(arr) - 1:
                    break

    print(f'#{tc}', *arr)