N = int(input())
result = []
cnt_3 = 0
cnt_6 = 0
cnt_9 = 0
for i in range(1, N+1):
    if '3' in str(i): 
        i = str(i).replace('3', '-')
    if '6' in str(i): 
        i = str(i).replace('6', '-')
    if '9' in str(i):
        i = str(i).replace('9', '-')
        
    print(i,end=' ')

    