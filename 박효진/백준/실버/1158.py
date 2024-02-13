K, N = map(int, input().split())
turn = N
# people = ?
# 지우고 남은 애들을 뒤에 이어붙이기 (2번 지워졌으면 2번 붙이기?)
sequence = []
for _ in range(K):
    sequence.append(people[turn])
    turn += N


print('<' + ', '.join(sequence) + '>')