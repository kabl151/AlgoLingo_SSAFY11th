import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
lst = []
result = []
# 우선순위 : 카운트, 길이, 사전순

# 글자 추가 및 글자수 M 미만 걸러내기
for i in range(N):
    wd = input().rstrip()
    if len(wd) >= M:
        lst.append(wd)

wd_lst = list(set(lst))
for i in wd_lst:
    cnt = lst.count(i)
    len_wd = len(i)
    result.append([cnt,len_wd,i])

while len(result) != 0:
    if result[-1][0] > result[-2][0]:
        print(result.pop())
    elif result[-1][0] == result[-2][0] and result[-1][1] > result[-2][1]:
        print(result.pop())
    elif result[-1][0] == result[-2][0] and result[-1][1] == result[-2][1]:
        result.sort()
        print(result.pop())