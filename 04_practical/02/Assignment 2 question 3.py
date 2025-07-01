def find_min(input_list):
    if input_list == []:
        return None
    min_value = input_list[0]
    for item in input_list[1:]:
        if item < min_value:
            min_value = item
    return min_value