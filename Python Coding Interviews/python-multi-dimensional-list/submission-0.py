from typing import List

# returns list of max element in each sublist
# returned in order the appear
def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    max_arr = []
    for arr in nested_arr:
        max_number = arr[0]
        for num in arr:
            max_number = max(max_number, num)
        max_arr.append(max_number)
    return max_arr

        


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
