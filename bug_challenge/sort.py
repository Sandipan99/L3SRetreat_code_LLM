def sort(lst):
    for num in range(len(lst)-1,0,-1):
       if lst[num]<lst[num-1]:
           temp = lst[num]
           lst[num] = lst[num-1]
           lst[num-1] = temp
    return lst

unsorted_list = [14, 46, 43, 27, 57, 41, 45, 21, 70]
sorted_list = sort(unsorted_list)

print(sorted_list)
