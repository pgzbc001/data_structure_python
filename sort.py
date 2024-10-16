def fubble_sort(array: list) -> None:
    n = len(array)

    for i in range(n - 1):
        exchang = 0
        for j in range(n - 1, i,  -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]
                exchang += 1
        if exchang == 0:
            break


lists = [1, 3, 4, 6, 7, 9, 8]
fubble_sort(lists)
print(lists)
