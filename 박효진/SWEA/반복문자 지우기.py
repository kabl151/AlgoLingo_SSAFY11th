T = int(input())
for tc in range(1, T+1):
    wd = input()
    for i in range(len(wd)-1):
        if wd[i] == wd[i+1]:
            continue
        else:
            