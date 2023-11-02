import math
from tkinter import S
from typing import Self

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

#save each equasion
#create a substitutuon for the remains
#from the second to last equasion, go backwards and use the substitutions for the numbers

class Eq:
    def __init__(self, nagyobb, kisebb, megvan, maradek):
        self.nagyobb = nagyobb
        self.kisebb = kisebb
        self.megvan = megvan
        self.maradek = maradek

    """
    nagyobb = oszto * megvanennyiszer + maradek

    nagyobb - oszto * megvanennyiszer = maradek

    substitution: nagyobb + oszto(substituted) * -megvan
    
    """

    pass