while True:
    n = int(input())
    if n == -1:
        break
    lst_int = []
    lst_str = []
    for i in range(1,n):
        if n % i == 0:
            lst_str.append(str(i))
            lst_int.append(i)
    result = ' + '.join(lst_str)
    if sum(lst_int) == n:
        print(f'{n} = ', end = '')
        print(result)
    else:
        print(f'{n} is NOT perfect.')