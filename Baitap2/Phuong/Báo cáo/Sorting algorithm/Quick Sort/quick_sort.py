def quickSort(a_list):
    quickSortHelper(a_list, 0, len(a_list)-1)

def quickSortHelper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)
        quickSortHelper(a_list, first, split_point - 1)
        quickSortHelper(a_list, split_point+1, last)

def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last

    done = False
    while not done:
        
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        
        while left_mark <= right_mark and a_list[right_mark] >= pivot_value:
            right_mark = right_mark -1
        
        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp
        
    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp

    return right_mark

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(a_list)
print(a_list)
        
