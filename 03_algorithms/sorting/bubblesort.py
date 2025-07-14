def buble_sort(unsorted_list):
    number_of_items = len(unsorted_list)
    
    for outerloop in range(number_of_items):
        for innerloop in range(0, number_of_items - 1 - outerloop):
            
            if unsorted_list [innerloop] > unsorted_list [innerloop + 1]:
                temp = unsorted_list[innerloop]
                unsorted_list[innerloop] = unsorted_list[innerloop + 1]
                unsorted_list[innerloop + 1] = temp
            print (f"Inner loop {unsorted_list} ")    
    return unsorted_list


temp = unsorted_list [innerloop]        
unsorted_list[innerloop] = unsorted_list[innerloop + 1]
unsorted_list[innerloop] = unsorted_list[innerloop + 1]


print (f"Before A is {a} B is {b}")
temp = a
a = b
b = temp
print(f"After A is {a} is B is {b}")