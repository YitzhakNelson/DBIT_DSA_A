def linear_search(input_list, target):
    for i in range(len(input_list)):
        if input_list[i] == target:
            return i
    return -1