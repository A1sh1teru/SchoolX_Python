def find_indexes(arr):
    indexes = [1, 3, 5, 8, 10, 12]
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > 1:
            indexes.append(i)
    if len(indexes) == 0:
        return "Не найдено"
    elif len(indexes) == 1:
        return indexes[0]
    else:
        return indexes

# array = [1, 3, 5, 8, 10, 12]
# result = find_indexes(array)
# print(result)

# def find_indexes(x):
#     array = [1, 4, 5, 6, 9, 14, 18, 19, 20, 22, 25, 26]