N = int(input())
card_lst = [x for x in range(1,N+1)]
for i in range(N-1):
    card_lst.pop(0)
    num = card_lst.pop(0)
    card_lst.append(num)
print(*card_lst)