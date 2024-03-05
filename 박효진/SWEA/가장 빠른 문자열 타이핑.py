T = int(input())
for tc in range(1, T+1):
    A, B = map(str, input().split())
    copy_count = A.count(B)
    result = A.replace(B, '', copy_count)

    print(f'#{tc} {len(result)+copy_count}')