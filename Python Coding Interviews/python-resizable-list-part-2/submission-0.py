from typing import List

# append elements of arr2 to end of arr1. use extend
def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    arr1.extend(arr2)
    return arr1
  
# remove all elements of arr2 from arr1. return arr1.
def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for elements in arr2:
        if elements in arr1:
            arr1.remove(elements)
    return arr1


# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))
