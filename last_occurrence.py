"""
    last occurrence
        [1,1,1,2,2,2,3,3,3,3,3,4] 3 => 10

"""




def last_occurrences(array,element):
    low , high = 0,len(array)-1
    
    while low <= high:
        mid =low+(high-low) //2
        
        if (array[mid] == element and mid ==len(array)-1) or \
            (array[mid] == element and array[mid+1] >element):
                return mid
        elif (array[mid]<=element):
            low = mid+1
        else :
            high = mid-1

print(last_occurrences([1,1,1,2,2,2,3,3,3,3,3,4],1))