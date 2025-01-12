"""
    binary search
        [1,3,5,7,8,9,11,12,15,22,30] 5=> 2 
"""


def binary_search(array,element) :
    low,high = 0,len(array)-1
    
    while low <= high :
        mid = low + (high-low) // 2
        val = array[mid]
        
        if element == val :
            return mid
        
        elif val < element :
            low = mid+1
            
        else:
            high = mid-1
    return -1
            
print(binary_search([1,3,5,7,8,9,11,12,15,22,30],1))