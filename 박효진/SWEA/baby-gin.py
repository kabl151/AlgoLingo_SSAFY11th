T = int(input())

for tc in range(1, T+1):
    num = list(map(int, input().rstrip()))
    result = []
    final = 'false'
    for i in range(6):
        for j in range(6):
            if i != j:
                for k in range(6):
                    if j != k and k != i:
                        for l in range(6):
                            if l != k and l != j and l != i:
                                for m in range(6):
                                    if m != l and m != k and m != j and m != i:
                                        for n in range(6):
                                            if n != m and n != l and n != k and n != j and n != i:
                                                result.append([num[i],num[j],num[k],num[l],num[m],num[n]])
    for i in result:
        cnt = 0
        if i[0] == i[1] - 1 and i[0] == i[2] -2:
            cnt += 1
        if i[0] == i[1] and i[1] == i[2]:
            cnt += 1
        if i[3] == i[4] -1 and i[3] == i[5] -2:
            cnt += 1
        if i[3] == i[4] and i[4] == i[5]:
            cnt += 1
        if cnt == 2:
            final = 'true'
    print(f'#{tc}', final)