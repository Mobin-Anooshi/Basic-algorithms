"""

    One time pad cipher

"""

import random

class Onetime :
    def encrypt(self,name):
        plain = [ord(i) for i in name]
        key = []
        cipher = [] 
        for i in plain:
            k = random.randint(1,300)
            c = (i +k)*k
            cipher.append(c)
            key.append(k)
        return cipher , key
    
    
c,k = Onetime().encrypt('mobin')
print(c)
print(k)