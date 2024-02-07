import sys
input = sys.stdin.readline

sentence = input().strip()
wd = input().strip()
wd_lst = list(wd)
lst = []
new_sentence = []
wd_len=len(wd)
for i in sentence:
    if len(lst) ==0 and i not in wd:
        new_sentence.append(i)
    elif len(lst) !=0 and i not in wd:
        new_sentence = new_sentence + lst
        lst.clear()
    elif i in wd and i == wd[0]:
        lst.append(i)
    elif i in wd and i != wd[0]:
        lst.append(i)
        if i == wd[-1]:
            lst_len = len(lst)
            if lst[lst_len-wd_len:lst_len+1:] == wd_lst:
                for _ in range(len(wd)):
                    lst.pop()
            else:
                new_sentence = new_sentence + lst

if len(new_sentence) != 0:
    print(*new_sentence, sep='')
else:
    print('FRULA')