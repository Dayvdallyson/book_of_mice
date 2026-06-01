def selection_sort(arr):

    arr = arr[:]

    for i in range(len(arr)):

        min_index = i

        for j in range(i + 1, len(arr)):

            if arr[min_index] > arr[j]:
                min_index = j

        print(arr[i], arr[min_index])
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print(selection_sort([42, 7, 91, 13, 58, 26, 74, 3, 65, 19, 88, 34, 50, 11, 97, 23, 61, 5, 79, 31, 46, 17, 92, 28, 54, 1, 83, 39, 67, 14, 95, 21, 48, 9, 72, 36, 60, 4, 85, 25, 53, 16, 99, 30, 70, 8, 44, 12, 76, 2]))
