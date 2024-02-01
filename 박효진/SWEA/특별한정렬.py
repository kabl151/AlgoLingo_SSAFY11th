T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))    
    for idx in range(N-1):
        if idx % 2 == 0: # max 나열
            max_idx = idx
            for i in range(idx + 1, N):
                if arr[max_idx] < arr[i]:
                    max_idx = i
            arr[idx], arr[max_idx] = arr[max_idx], arr[idx]
        else:            # min 나열
            min_idx = idx
            for j in range(idx + 1, N):
                if arr[min_idx] > arr[j]:
                    min_idx = j
            arr[idx], arr[min_idx] = arr[min_idx], arr[idx]
    new_arr = arr[:10:]
    new_arr =' '.join(map(str, new_arr))
    print(f'#{tc} {new_arr}')
