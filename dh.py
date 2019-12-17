import math
import decimal

def compute_shared(g, p, k):
	return (g ** k ) % p

def sophie_germain(p,n):
	for i in range(n):
		p = (2*p) + 1
	return p
p = sophie_germain(23,50) #computes a large prime number
# p = decimal.Decimal(2**1536 - 2**1472 - 1 + 2**64 * { decimal.Decimal[2**(1406*math.pi)] + 741804 })
print(p)
g = 5 # A primitive root of 23
a = 4
b = 3
bob = compute_shared(g,p,b)
alice = compute_shared(g,p,a)
alice_shared_secret = compute_shared(bob,p,a)
bob_shared_secret = compute_shared(alice,p,b)
if (alice_shared_secret == bob_shared_secret):
	print(alice_shared_secret)
