"""
    first occurrence
        [1,1,1,2,2,2,3,3,3,3,3,4] 3 => 6

"""

def first_occurrences(array,element):
    low , high = 0,len(array)-1
    
    while low <= high:
        mid =low+(high-low) //2
        
        if low == high :
            break
        
        elif array[mid] < element :
            low = mid +1 
            
        else :
            high = mid  
            
    
    if  array[low] == element :
        return low
    
print(first_occurrences([1,1,1,2,2,2,3,3,3,3,3,4],4))
    