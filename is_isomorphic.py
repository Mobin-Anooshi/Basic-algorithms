"""
    is isomorphic
        foo,bar => False
        foo,bee => True
        
"""


def is_isomorphic(s,t):
    
    if len(s) != len(t):
        return False
    
    dict = {}
    set_value = set()
    
    for i in range(len(s)):
        if s[i] not in dict :
            if t[i] in set_value :
                return False
            dict[s[i]] = t[i]
            set_value.add(t[i])
        else:
            if dict[s[i]] != t[i]:
                return False
    return True
print(is_isomorphic('foe','beq'))