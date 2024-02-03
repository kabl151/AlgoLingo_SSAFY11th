import sys
input = sys.stdin.readline

lst = []
for _ in range(3):
    angle = int(input())
    lst.append(angle)
lst.sort()
if lst[0] == 60 and lst[1] == 60 and lst[2] == 60:
    print('Equilateral')
elif sum(lst) == 180 and (lst[0] == lst[1] or lst[1] == lst[2]):
    print('Isosceles')
elif sum(lst) == 180 and (lst[0] != lst[1] and lst[1] != lst[2] and lst[2] != lst[0]):
    print('Scalene')
elif sum(lst) != 180:
    print('Error')