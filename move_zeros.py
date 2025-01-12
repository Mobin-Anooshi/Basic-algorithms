"""
    move zero
        [False,1,0,0,1,1,0,1,0,1,1,1,] => [False,1,1,1,1,1,1,0,0,0,0]

"""

def move_zero(seq):
    result = []
    zeros = 0
    for i in seq:
        if i == 0 and type(i) != bool :
            zeros += 1
        else:
            result.append(i)
    result.extend([0]* zeros)
    return result

print(move_zero([False,1,0,0,1,1,0,1,0,1,1,1,]))