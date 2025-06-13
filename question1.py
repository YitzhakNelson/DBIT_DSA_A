def rotate_left_pop(lst):
    if not lst:
        return lst
    lst.append(lst.pop(0))
    return lst