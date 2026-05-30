def binary_search(list_numbers, my_number) -> str:
    low = 0
    high = len(list_numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        guess = list_numbers[mid]

        if guess == my_number:
            return f"This is ur number {guess}! "

        if my_number < guess:
            high = mid - 1

        if guess < my_number:
            low = mid + 1

    return "Ur number was not found"

my_list_numbers = [ 3, 7, 12, 18, 23, 29, 34, 41, 56, 72]

print(binary_search(my_list_numbers, 23))
