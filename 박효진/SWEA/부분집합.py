def selection(i, t, subset):
    if i == len(lst):
        if sum(subset) == t:
            print(subset)
    elif sum(subset) > t:
        return
    else:
        subset.append(lst[i])
        selection(i+1, t, subset)
        subset.pop()
        selection(i+1, t, subset)

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
subset = []
t = 10
selection(0, t, subset)