def per(lst,visited,result, target,oper_seq):
    if len(result) == target:
        oper_seq.append([result])
    for i in range(len(lst)):
        if visited[i] == False:
            visited[i] = True
            result.append(lst[i])
            per(lst,visited,result,target,oper_seq)
            visited[i] = False
            result.pop()

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    oper = list(map(int, input().split()))
    oper_lst = []
    oper_str = ['+','-','*','/']
    for i in range(4):
        for _ in range(oper[i]):
            oper_lst.append(oper_str[i])
    num_lst = list(map(int, input().split()))
    result = []
    oper_seq = []
    visited = [False]*len(oper)
    lst = [x for x in range(len(oper))]
    target = len(oper)
    per(lst,visited,result,target,oper_seq)
    print(oper_seq)