T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    lst = []
    result = []
    for i in range(N):
        for j in range(i+1, N):
            lst.append(str(arr[i] * arr[j]))
    for i in range(len(lst)):
        




    # for i in range(len(lst)):
    #     if len(lst[i]) >= 2:
    #         jd = 1
    #         for j in range(1, int(lst[i])):
    #             if int(lst[i][j+1]) < int(lst[i][j-1]):
    #                 jd = 0
    #             else:
    #                 pass
    #         if jd == 1:
    #             result.append(i)
    #         else:
    #             pass
    #     else:
    #         result.append(i)
    # print(result)
