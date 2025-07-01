def has_duplicates(input_list):
    for i in range(len(input_list)):
        for j in range(i):
            if input_list[i] == input_list[j]:
                return True
    return False