def find_max(input_list):
    if input_list == []:
        return None
    max_value = input_list[0]
    for item in input_list[1:]:
        if item > max_value:
            max_value = item
    return max_value