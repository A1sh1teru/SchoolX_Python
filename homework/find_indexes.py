def find_index(arr):
    index_list = [i for i in range(1, len(arr)) if arr[i] - arr[i - 1] > 1]
    if not index_list:
        return "Не найдено"
    elif len(index_list) == 1:
        return index_list[0]
    else:
        return index_list
    
arr = [-19, -18, -17, -16,  -10, 0, 20]
print(find_index(arr))