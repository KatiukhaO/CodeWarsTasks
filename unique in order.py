def unique_in_order(iterable):
    res_list = []
    res_list.append(iterable[0])
    for char in iterable:
        if char != res_list[-1]:
            res_list.append(char)
    return res_list


print(unique_in_order('AAAABBBCCDAABBB'))     #, ['A','B','C','D','A','B'])