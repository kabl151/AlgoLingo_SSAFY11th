import sys
input = sys.stdin.readline

P = int(input())
for tc in range(1,P+1):
    line = []
    cnt = 0
    info = list(map(int, input().split()))[1::]
    for i in range(20):
        num = info[i]
        line.append(num)
        for j in range(len(line)-1):
            if line[-j-2] > line[-j-1]:
                line[-j-2], line[-j-1] = line[-j-1], line[-j-2]
                cnt += 1
    print(tc, cnt)