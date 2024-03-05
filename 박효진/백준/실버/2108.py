import sys
input = sys.stdin.readline

N = int(input())
lst = []
num_lst = [0] * 8001

for i in range(N):
    num = int(input())
    num_lst[num + 4000] += 1
    lst.append(num)

lst.sort()
if sum(lst)/sum(num_lst) <= 0 and sum(lst)/sum(num_lst) > -(1/2):
    print(0)
else:
    print(f'{sum(lst)/sum(num_lst):.0f}')

print(lst[(N-1)//2])
#최빈값
if len(lst) != 1:
    idx=num_lst.index(max(num_lst))
    try:
        idx_2=num_lst.index(max(num_lst), idx+1, 8000)
        if num_lst[idx] == num_lst[idx_2]:
            print(idx_2-4000)
        else:
            print(idx-4000)
    except ValueError:
        print(idx - 4000)
else:
    print(*lst)
print(max(lst) - min(lst))