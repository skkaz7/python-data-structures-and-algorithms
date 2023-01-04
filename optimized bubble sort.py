def optimized_bubble_sort(num_list):
    for i in range(len(num_list)):
        swapped = False
        for j in range(len(num_list) - i - 1):
            if num_list[j] > num_list[j + 1]:
                num_list[j], num_list[j + 1] = num_list[j + 1], num_list[j]

                swapped = True

        if not swapped:
            break


if __name__ == '__main__':
    data = [-2, 45, 0, 11, -9]
    optimized_bubble_sort(data)
    print('Sorted Array in Ascending Order:')
    print(data)
