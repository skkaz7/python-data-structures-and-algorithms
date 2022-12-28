def binary_search_algorithm(num, sorted_num_list):
    left = 0
    right = len(sorted_num_list) - 1

    while left <= right:
        middle = (left + right) // 2
        if num == sorted_num_list[middle]:
            print(f'Number {num} is on the list!')
            break
        elif num < sorted_num_list[middle]:
            right = middle - 1
        else:
            left = middle + 1

    else:
        print(f'Number {num} is not on the list!')


if __name__ == '__main__':
    some_sorted_list = [-10, -7, -5, -3, 0, 3, 5, 21, 68, 341, 500]
    binary_search_algorithm(-7, some_sorted_list)
