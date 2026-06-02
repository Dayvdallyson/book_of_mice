def binary_search(my_array, my_item):

    low = 0
    high = len(my_array) - 1

    while low <= high:

        mid = (low + high) // 2

        guess = my_array[mid]

        if guess == my_item:
            return f"U found ur item: {my_item}"

        if guess > my_item:
            high = mid - 1

        if guess < my_item:
            low = mid + 1

    return "Ur item was not found"

my_ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search(my_ordered_list, 7))
