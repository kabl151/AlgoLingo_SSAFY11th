N, L = map(int,input().split())
h = list(map(int,input().split()))

sort_h = sorted(h)
for i in sort_h:
    if i <= L:
        L += 1
print(L)