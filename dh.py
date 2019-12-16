def compute_shared(g, p, k):
	return (g ** k ) % p

p = 23
g = 5 # A primitive root of 23
a = 4
b = 3
bob = compute_shared(g,p,b)
alice = compute_shared(g,p,a)
alice_shared_secret = compute_shared(bob,p,a)
bob_shared_secret = compute_shared(alice,p,b)
if (alice_shared_secret == bob_shared_secret):
	print(alice_shared_secret)
