import sys
input = sys.stdin.readline

N = int(input())
deck = []
for _ in range(N):
    keyword = input().split()
    if keyword[0] == '1':
        deck.insert(0,keyword[1])
    elif keyword[0] == '2':
        deck.append(keyword[1])
    elif keyword[0] == '3':
        if deck:
            num = deck.pop(0)
            print(num)
        else:
            print(-1)
    elif keyword[0] == '4':
        if deck:
            num = deck.pop(-1)
            print(num)
        else:
            print(-1)
    elif keyword[0] == '5':
        print(len(deck))
    elif keyword[0] == '6':
        if deck:
            print(0)
        else:
            print(1)
    elif keyword[0] == '7':
        if deck:
            print(deck[0])
        else:
            print(-1)
    elif keyword[0] == '8':
        if deck:
            print(deck[-1])
        else:
            print(-1)