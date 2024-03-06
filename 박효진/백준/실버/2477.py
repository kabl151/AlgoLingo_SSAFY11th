import sys
input = sys.stdin.readline
K = int(input())

info = []
for i in range(6):
    info.append(list(map(int, input().split())))

if info[0][0] == 1:
    if info[1][0] == 3:
        if info[2][0] == 1:
            if info[3][0] == 3:
                print(K*(info[4][1]*info[5][1]-info[1][1]*info[2][1]))
            elif info[3][0] == 4:
                print(K*(info[3][1]*info[4][1]-info[0][1]*info[1][1]))
                
        elif info[2][0] == 2:
            if info[2][1] < info[0][1]:
                if info[3][0] == 3:
                    print(K*(info[0][1]*info[5][1]-info[2][1]*info[3][1]))
                elif info[3][0] == 4:
                    print(K*(info[0][1]*info[1][1]-info[3][1]*info[4][1]))

            else:
                if info[5][0] == 3:
                    print(K*(info[2][1]*info[3][1]-info[0][1]*info[5][1]))
                elif info[5][0] == 4:
                    print(K*(info[1][1]*info[2][1]-info[4][1]*info[5][1]))

    elif info[1][0] == 4:
        if info[2][0] == 1:
            if info[3][0] == 3:
                print(K*(info[3][1]*info[4][1]-info[0][1]*info[1][1]))
            
            elif info[3][0] == 4:
                print(K*(info[4][1]*info[5][1]-info[1][1]*info[2][1]))

        elif info[2][0] == 2:
            if info[2][1] < info[0][1]:
                if info[3][0] == 3:
                    print(K*(info[0][1]*info[1][1]-info[3][1]*info[4][1]))
                elif info[3][0] == 4: 
                    print(K*(info[0][1]*info[5][1]-info[2][1]*info[3][1]))
                    
            else:
                if info[5][0] == 3:
                    print(K*(info[1][1]*info[2][1]-info[4][1]*info[5][1]))
                elif info[5][0] == 4:
                    print(K*(info[2][1]*info[3][1]-info[0][1]*info[5][1]))
            
elif info[0][0] == 2:
    if info[1][0] == 3:
        if info[2][0] == 1:
            if info[2][1] < info[0][1]:
                if info[3][0] == 3:
                    print(K*(info[0][1]*info[5][1]-info[2][1]*info[3][1]))
                elif info[3][0] == 4:
                    print(K*(info[0][1]*info[1][1]-info[3][1]*info[4][1]))                    
            else:
                if info[5][0] == 3:
                    print(K*(info[2][1]*info[3][1]-info[0][1]*info[5][1]))
                elif info[5][0] == 4:
                    print(K*(info[1][1]*info[2][1]-info[4][1]*info[5][1]))

        elif info[2][0] == 2:
            if info[3][0] == 3:
                print(K*(info[4][1]*info[5][1]-info[1][1]*info[2][1]))
            
            elif info[3][0] == 4:
                print(K*(info[3][1]*info[4][1]-info[0][1]*info[1][1]))

    elif info[1][0] == 4:
        if info[2][0] == 1:
            if info[2][1] < info[0][1]:
                if info[3][0] == 3:
                    print(K*(info[0][1]*info[1][1]-info[3][1]*info[4][1]))
                elif info[3][0] == 4:    
                    print(K*(info[0][1]*info[5][1]-info[2][1]*info[3][1]))
            else:
                if info[5][0] == 3:
                    print(K*(info[1][1]*info[2][1]-info[4][1]*info[5][1]))
                elif info[5][0] == 4:
                    print(K*(info[2][1]*info[3][1]-info[0][1]*info[5][1]))

        elif info[2][0] == 2:
            if info[3][0] == 3:
                print(K*(info[3][1]*info[4][1]-info[0][1]*info[1][1]))
            elif info[3][0] == 4:
                print(K*(info[4][1]*info[5][1]-info[1][1]*info[2][1]))

elif info[0][0] == 3:
    if info[1][0] == 1:
        if info[2][0] == 3:
            if info[3][0] == 1:
                print(K*(info[4][1]*info[5][1]-info[1][1]*info[2][1]))

            elif info[3][0] == 2:
                print(K*(info[3][1]*info[4][1]-info[0][1]*info[1][1]))

        elif info[2][0] == 4:
            if info[2][1] < info[0][1]:
                if info[3][0] == 1:
                    print(K*(info[0][1]*info[5][1]-info[2][1]*info[3][1]))
                elif info[3][0] == 2:
                    print(K*(info[0][1]*info[1][1]-info[3][1]*info[4][1]))
            else:
                if info[5][0] == 1:
                    print(K*(info[2][1]*info[3][1]-info[0][1]*info[5][1]))
                elif info[5][0] == 2:
                    print(K*(info[1][1]*info[2][1]-info[4][1]*info[5][1]))

    elif info[1][0] == 2:
        if info[2][0] == 3:
            if info[3][0] == 1:
                print(K*(info[3][1]*info[4][1]-info[0][1]*info[1][1]))
            elif info[3][0] == 2:
                print(K*(info[4][1]*info[5][1]-info[1][1]*info[2][1]))
        elif info[2][0] == 4:
            if info[2][1] < info[0][1]:
                if info[3][0] == 1:
                    print(K*(info[0][1]*info[1][1]-info[3][1]*info[4][1]))
                elif info[3][0] == 2:
                    print(K*(info[0][1]*info[5][1]-info[2][1]*info[3][1]))
            else:
                if info[5][0] == 1:
                    print(K*(info[1][1]*info[2][1]-info[4][1]*info[5][1]))
                elif info[5][0] == 2:
                    print(K*(info[2][1]*info[3][1]-info[0][1]*info[5][1]))

elif info[0][0] == 4:
    if info[1][0] == 1:
        if info[2][0] == 3:
            if info[2][1] < info[0][1]:
                if info[3][0] == 1:
                    print(K*(info[0][1]*info[5][1]-info[2][1]*info[3][1]))
                elif info[3][0] == 2:
                    print(K*(info[0][1]*info[1][1]-info[3][1]*info[4][1]))
            else:
                if info[5][0] == 1:
                    print(K*(info[2][1]*info[3][1]-info[0][1]*info[5][1]))
                elif info[5][0] == 2:
                    print(K*(info[1][1]*info[2][1]-info[4][1]*info[5][1]))

        elif info[2][0] == 4:        
            if info[3][0] == 1:
                print(K*(info[4][1]*info[5][1]-info[1][1]*info[2][1]))
            elif info[3][0] == 2:
                print(K*(info[3][1]*info[4][1]-info[0][1]*info[1][1]))

    elif info[1][0] == 2:
        if info[2][0] == 3:
            if info[2][1] < info[0][1]:
                if info[3][0] == 1:
                    print(K*(info[0][1]*info[1][1]-info[3][1]*info[4][1]))
                elif info[3][0] == 2:
                    print(K*(info[0][1]*info[5][1]-info[2][1]*info[3][1]))
            else:
                if info[5][0] == 1:
                    print(K*(info[1][1]*info[2][1]-info[4][1]*info[5][1]))
                elif info[5][0] == 2:
                    print(K*(info[2][1]*info[3][1]-info[0][1]*info[5][1]))

        elif info[2][0] == 4:
            if info[3][0] == 1:
                print(K*(info[3][1]*info[4][1]-info[0][1]*info[1][1]))
            elif info[3][0] == 2:
                print(K*(info[4][1]*info[5][1]-info[1][1]*info[2][1]))