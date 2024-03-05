N = int(input())
lst = []
movie_num = 666
while True:
    judge = str(movie_num).find('666')
    if judge != -1:
        lst.append(movie_num)
    movie_num += 1
    if len(lst) == N:
        break
print(lst[-1])