def sort_tuple(in_tuple):
    chan_list = list(in_tuple)
    chan_list.sort()
    new_tuple = tuple(chan_list)
    return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)
