"""
    Top One
        [1,2,3,1,2] => [1,2]

"""


def top(arr):
    value = {}
    result = []
    f_value = 0
    
    for i in arr:
        if i in value:
            value[i] += 1
        else :
            value[i] = 1
        
    f_value = max(value.values())

    for  i in value.keys():
        if value[i] == f_value :
            result.append(i)
        else :
            continue
    
    return result,f_value


print(top([1,2,3,4,4,5,3,2,4,2]))