T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    w = list(map(int, input().split()))
    t = list(map(int, input().split()))
    w.sort()
    w.reverse()
    t.sort()
    t.reverse()
    result = []
    judge = [False]*len(t)
    for i in range(len(t)):
        for j in range(len(w)):
            if judge[i] == False and t[i] >= w[j]:
                judge[i] = True
                result.append(w[j])

    print(sum(result))