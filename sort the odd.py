

def sort_array(source_array):
    # Return a sorted array.
    if not source_array:
        return source_array
    else:
        odd = [x for x in source_array if x%2 !=0]
        odd.sort(reverse=True)
        for j, elem in enumerate(source_array):
            if elem %2 != 0:
                source_array.pop(j)
                source_array.insert(j, odd.pop(-1))
        return source_array

print(sort_array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])) #[1, 8, 3, 6, 5, 4, 7, 2, 9, 0]
