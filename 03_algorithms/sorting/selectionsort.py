def selection_sort(unsorted_list):
    number_of_items = len(unsorted_list)
    
    for outerloop in range(number_of_items):
        minimum_index = outerloop
        for innerloop in range(outerloop + 1, number_of_items):
            if unsorted_list[innerloop] < unsorted_list[minimum_index]:
                minimum_index = innerloop
        for innerloop in range(0, number_of_items - 1 - outerloop):
            
            temp = unsorted_list[outerloop]
            unsorted_list[outerloop] = unsorted_list[minimum_index]
            unsorted_list[minimum_index] = temp
            print(f"Outer loop {unsorted_list} ")
    return unsorted_list


values = [5,4,3,2,1]
print (f"Unsorted list {values}")

sorted_list = selection_sort(values)
print (f"Sorted list {sorted_list}")