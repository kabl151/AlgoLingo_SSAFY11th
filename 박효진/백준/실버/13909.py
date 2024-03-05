N = int(input())
window = [0]*(N+1)
seq = [x for x in range(1,N+1)]
for i in seq:
    for j in range(i,N+1,i):
        if window[j] == 1:
            window[j] = 0
        else:
            window[j] = 1
print(sum(window))
#-----------------------------------

import math
print(int(math.sqrt(int(input()))))