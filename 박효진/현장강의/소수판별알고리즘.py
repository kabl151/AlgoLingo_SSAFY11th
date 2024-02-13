# 소수 : 1과 자기 자신을 제외한 다른 정수로 나누어지지 않는 않는 수

# 간단한 소수 판별 방법?
# 주어진 수 N일때 N보다 작은 수(2 ~ 최대 N-1)에 대해 모두 나누어보고, 
# 나눠떨어지지 않는다면 소수!!

def is_prime(N):
    for i in range(2,int(N**0.5) + 1):  # N**0.5 가 N의 최대로 나눌 수 있는 수(제곱근)이기 때문
        if N % i == 0:
            return False
    return True #소수다!

print(is_prime(N))

# -------------------------
# 만약 하나의 수가아니라 범위내 수를 하려면
for num in range(M):   #을 하게되면 bigO(제곱근 num * M)
    is_prime(num)

# 이를 위해 에라토스테네스의 체
# : 소수를 판별하는 알고리즘 = N 보다 작은 소수들을 모두 판별
# 1. 2부터 시작해서 연속된 정수들 중에서 아직 소수로 판별되지 않은 수를 찾는다.
# 2. 그 수를 소수로 판별 시키고 그 수의 배수들은 모두 소수가 아니다.
# 3. 1단계와 2단계 과정을 N 범위 내에서 계속 반복하면서 모든 소수를 판별

def sieve(N):
# 소수인지를 체크해두는 리스트를 하나 만듦 is_prime
    is_prime = [True] * (N + 1)
    # 0 과 1은 소수가 아니므로 미리 처리
    is_prime[0] = is_prime[1] = False
    for i in range(2,int(N**0.5) + 1):
    # 아직 소수로 판별되지 않은 가장 작은 수를 찾는다. 그 수를 소수로 판별시킨다
        if is_prime[i] == True: # 소수다
            # 해당되는 소수를 가지고 "그 수의 배수들은 모두 소수가 아니라고 판별한다."
            for j in range(i + i, N + 1, i):
                # 2배 , 3배, ...(N까지)
                is_prime[j] = False
        # 소수인 값만 리스트로 만들어주기..
    primes = []
    for i in range(2, N + 1):
        if is_prime[i]:
            primes.append(i)
    return primes            

N = 30
primes = sieve(N)
print(primes)
    