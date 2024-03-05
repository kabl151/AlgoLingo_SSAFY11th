lst_x = []
lst_y = []
for _ in range(3):
    x, y = map(int, input().split())
    lst_x.append(x)
    lst_y.append(y)
final_x = 0
final_y = 0
if lst_x[0] == lst_x[1]:
    final_x = lst_x[2]
elif lst_x[1] == lst_x[2]:
    final_x = lst_x[0]
else:
    final_x = lst_x[1]

if lst_y[0] == lst_y[1]:
    final_y = lst_y[2]
elif lst_y[1] == lst_y[2]:
    final_y = lst_y[0]
else:
    final_y = lst_y[1]

print(final_x, final_y)