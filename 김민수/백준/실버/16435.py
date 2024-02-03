n, l = map(int, input().split())
h = map(int, input().split())
for x in sorted(h):
    if l >= x:
        l += 1
    else:
        break
print(l)
