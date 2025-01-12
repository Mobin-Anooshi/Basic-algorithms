""" 
    a1z26
        amir <==> [97,109,105,114]

"""


def encode(plain):
    return [ord(elm) for elm in plain]


def decode(plain):
    return "".join([chr(elm) for elm in plain])

print(encode('mobin'))
print(decode([109, 111, 98, 105, 110]))