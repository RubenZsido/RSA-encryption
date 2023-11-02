import random
from ExtendedEuclideanAlgorithm import gcdExtended
from EuclideanAlgorithm import gcd

def mod_inverse(e, phi_n):
    g, x, y = gcdExtended(e, phi_n)
    if g != 1:
        raise ValueError("The modular inverse does not exist")
    else:
        return x % phi_n


p = 11
q = 13
if p == q:
    print("p and q must be different")

n = p * q
phi_n = (p-1)*(q-1)

e = 23
if not gcd(e,phi_n) == 1:
    print("e's and z's gdc must be one")

#I don't fully understand this part yet
d = mod_inverse(e, phi_n)

if not (d * e - 1) % phi_n == 0:
    print("e × d − 1 must be a multiple of φ(n)")
print("Public key: (", n, ", ", e, ")")
print("Secret Key: (", n, ",", d, ")" )
m = 5
me = pow(m, e) % n

md = pow(me, d) % n

print("me:", me)
print("md:", md)