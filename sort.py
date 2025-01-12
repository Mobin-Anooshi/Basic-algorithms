"""
    bead sort
        [1,10,5,7,2,4,9] => [1,2,4,5,7,9]     
"""



def bead_sort(sequence):
    if any(not isinstance(x,int) or x<0 for x in sequence):
        raise TypeError('ERROR')
    
    for _ in range(len(sequence)) :
        for i,(rod_upper,rod_lower) in enumerate(zip(sequence,sequence[1:])):
            if rod_upper >rod_lower :
                sequence[i] -= rod_upper - rod_lower
                sequence[i + 1] += rod_upper - rod_lower 
    return sequence

print(bead_sort([1,10,5,7,2,4,9]))    
            