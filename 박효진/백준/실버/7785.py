import sys
input = sys.stdin.readline

n = int(input())
company = []
for i in range(n):
    info = list(input().split())
    if info[1] == 'enter':
        company.append(info[0])
    else:
        company.remove(info[0])
company.sort()
company.reverse()
for i in range(len(company)):
    print(company[i])