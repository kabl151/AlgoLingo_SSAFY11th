T = int(input())
dct = {'0' : 0,
       '1' : 1,
       '2' : 2,
       '3' : 3,
       '4' : 4,
       '5' : 5,
       '6' : 6,
       '7' : 7,
       '8' : 8,
       '9' : 9,
       'A' : 10,
       'B' : 11,
       'C' : 12,
       'D' : 13,
       'E' : 14,
       'F' : 15}
for tc in range(1, T+1):
    length, num_16 = map(str, input().split())
    result = ''
    for i in range(int(length)):
        num_2 = ''
        num_10 = dct[num_16[i]]
        for j in range(4):
            num_2 += str(num_10 % 2)
            num_10 //= 2
        result += num_2[::-1]
    print(f'#{tc}', result)