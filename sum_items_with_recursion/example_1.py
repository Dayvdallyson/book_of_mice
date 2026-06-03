my_numbers = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def sum_my_numbers(numbers, i=0):
    if i == len(numbers):
        return 0
    return numbers[i] + sum_my_numbers(numbers, i + 1)

print(sum_my_numbers(my_numbers))
