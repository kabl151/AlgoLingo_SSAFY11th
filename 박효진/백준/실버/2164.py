# N = int(input())
# card_lst = [x for x in range(1,N+1)]
# for i in range(N-1):
#     card_lst.pop(0)
#     card_lst.append(card_lst.pop(0))
# print(*card_lst)

#----------------------------------------

# import sys
# input = sys.stdin.readline

# N = int(input())
# card_lst = [x for x in range(1,N+1)]
# for i in range(N-2):
#     card_lst = card_lst[2::] + [card_lst[1]]

# print(card_lst[1])

#-------------------------------------------
# import sys
# input = sys.stdin.readline

# N = int(input())
# card_lst = [x for x in range(1,N+1)]
# for i in range(N-1):
#     card_lst.pop(0)
#     card_lst.append(card_lst.pop(0))
# print(*card_lst)

#-------------------------------------------

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
card_lst = [x for x in range(1, N+1)]
d = deque(card_lst)
for i in range(N-1):
    d.popleft()
    d.rotate(-1)
print(*d)