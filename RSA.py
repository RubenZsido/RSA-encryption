import random
#Step 1
#Public key
# Choose two large prime numbers (p and q)
p = 13
q = 17

#Step 2
# Calculate n = p*q and z = (p-1)(q-1)
n = p * q #11 * 13 7 143
z = (p-1)*(q-1) #10 * 12 = 120

#Step 3
# Choose a number e where 1 < e < z.
#randint includes both parameters
#e = random.randint(2, z+1)
e = 5
#Step 4
#calculate secret key
# Calculate d = e-1mod(p-1)(q-1)
d = e-1 % (p-1) * (q-1)

# You can bundle private key pair as (n,d)
print("Private keys: (", n, ", ", d, ")")
# You can bundle public key pair as (n,e)

#plaintext: m
m = 10
cyphertext = m * e % n
print(cyphertext)
