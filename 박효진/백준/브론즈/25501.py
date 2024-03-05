def recursion(wd):
    if len(wd) % 2 == 0:
        
    else:

        cnt += 1


def isPalindrome(wd):
    return recursion(wd)

T = int(input())
for _ in range(T):
    wd = input()
    cnt = 0
    print(isPalindrome(wd))