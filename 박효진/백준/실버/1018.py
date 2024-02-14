import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
solution_1 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
solution_2 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]


fix_lst = []
for i in range(N-8+1):
    for j in range(M-8+1):
        test_arr = arr[i][j]
        fix_num = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if solution_1[k-i][l-j] == arr[k][l]:
                    continue
                else:
                    fix_num += 1
        fix_lst.append(fix_num)

        fix_num = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if solution_2[k-i][l-j] == arr[k][l]:
                    continue
                else:
                    fix_num += 1
        fix_lst.append(fix_num)
print(min(fix_lst))