def binary_search(list_items, item):
    low = 0
    high = len(list_items) - 1


    while low <= high:
        mid = (low + high) // 2
        guess = list_items[mid]

        if guess == item:
            return mid

        if guess > item:
            high = mid - 1

        else:
            low = mid + 1

    return -1
