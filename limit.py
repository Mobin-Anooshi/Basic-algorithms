"""
    [1,2,3,4,5,6]
        min 3 => [3,4,5,6]
        max 3 => [1,2,3]
        max,min 3 => [3]

"""

def limit (arr , min=None , max=None):
    min_check = lambda val : True if min is None else (val>=min)
    max_check = lambda val : True if max is None else(val<=max)
    
    return [val for val in arr if min_check(val) and max_check(val)]

print(limit([1,2,3,4,5,6,7,8,9],min=3,max=5))