# import sys
# input = sys.stdin.readline

# word = str(input().strip())
# word = word.lower()
# set_word = set(word)
# reset_word = list(set_word)
# a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26
# arr = [0 for _ in range(26)]

# arr[m-1] += 1
# print(arr[12])


# -----------------------------------------------
word = str(input())
word = word.upper()
set_word = set(word)
lst_word = list(set_word)

cnt_lst = []
for i in lst_word:
    cnt = 0
    for j in range(len(word)):
        if i == word[j]:
            cnt +=1
    cnt_lst.append(cnt)
max_cnt = max(cnt_lst)
if len(cnt_lst) == 1:
    print(*lst_word)
elif len(cnt_lst) >= 2:
    sorted_lst = sorted(cnt_lst)
    if sorted_lst[-1] == sorted_lst[-2]:
        print('?')
    else:
        idx = 0
        for j in range(len(cnt_lst)):
            if cnt_lst[j] == max_cnt:
                idx = j
        print(lst_word[idx])            
    