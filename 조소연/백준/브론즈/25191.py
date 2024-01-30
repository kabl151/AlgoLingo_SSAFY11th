N = int(input())
lst = list(map(int, input().split()))

cola = lst[0] // 2
beer = lst[1]

chicken = cola + beer

if N < chicken :
    chicken = N

print(chicken)