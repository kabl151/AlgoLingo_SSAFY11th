# 유클리드 호제법 최대공약수 (GCD: Greatedst Common Divisor)
#                최소공배수 (LCM: Least Common Multiple)
# 유클리드 호제법은 다음과 같이 작동합니다:

# 두 수 a와 b의 최대공약수를 구하려면, a를 b로 나눕니다. 이때 나머지를 r이라고 합니다.
# 만약 r이 0이면, b가 a와 b의 최대공약수입니다. 
# 그렇지 않으면, a를 b로, b를 r로 대체하고 다시 나누기를 반복합니다.
# 이 과정을 나머지가 0이 될 때까지 반복합니다.
# 이 알고리즘은 두 수의 크기에 관계없이 빠르게 최대공약수를 찾을 수 있습니다. 
# 또한, 이 알고리즘을 확장하여 최소공배수(LCM, Least Common Multiple)를 구할 수도 있습니다. 
# 최소공배수는 두 수의 곱을 최대공약수로 나눈 것과 같습니다.
# a를 큰수로 가정
# a%b = r나머지 (0이라면 b가 a의 최대 공약수)
# b%r = 
import sys
input = sys.stdin.readline

A, B = map(int, input().split())
result = 0
test_A = A
test_B = B
if A > B:
    while True:
        r = A % B
        if r == 0:
            result = B
            break
        else:
            A = B
            B = r
else:
    A, B = B, A
    while True:
        r = A % B
        if r == 0:
            result = B
            break
        else:
            A = B
            B = r
print(test_A * test_B // result)