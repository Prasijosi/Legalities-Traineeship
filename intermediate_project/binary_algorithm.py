def binary_search(numbers_list, target):
    start = 0
    end = len(numbers_list) - 1

    while start <= end:
        # Find the middle index of the current range
        middle = start + (end - start) // 2
        # Get the value at the middle index
        middle_value = numbers_list[middle]

        if middle_value == target:
            return middle 
        
        elif target < middle_value:
            end = middle - 1
        
        # If the target is larger than the middle value, search the upper half
            start = middle + 1

    # Return 0 if the target is not found in the list
    return "Not found in the list"

# List of sorted numbers to search in
numbers_list = [2, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]

target_number = int(input("Enter a number: "))

print(binary_search(numbers_list, target_number))
