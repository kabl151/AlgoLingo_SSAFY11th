N = int(input())
wd_cnt = 0
for i in range(1,N+1):
    wd = input()
    wdq = wd +'Q'
    for i in range(len(wd)):
        if wdq[i] == wdq[i+1] or wdq[i+1] == 'Q':
            continue
        elif wdq[i] != wdq[i+1]:
            cnt = 0
        for j in range(i+2,len(wdq)):
            if wdq[i] == wdq[j]:
                cnt += 1
        if cnt == 0:
            wd_cnt +=1
        elif cnt != 0:
            pass

print(wd_cnt)