import math

def gcd(a, b):
    print("(",a,",",b,")")
    #switch them if b is bigger
    if b > a:
        c = a
        a = b
        b = c
    remains = a % b
    #if the remains is 0, than the last remains is the gdc
    if remains == 0:
        print(b)
        return
    #if what remains is not 0, repeat the algorithm, by giving it the smaller number(b) and the remains
    gcd(b, remains)
    

gcd(54, 888)

