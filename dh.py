import math
import decimal
import random
import time
import os

#Thix is the Whole Algorithm
def compute_shared(g,p,k):
	return (g ** k ) % p

def compute_random():
	return random.randint(0,1000)

def sophie_germain(p,n):
	for i in range(n):
		p = (2*p) + 1
	return p
p = sophie_germain(23,15) #computes a large prime number
g = 14 # A primitive root of 786431
print("The prime number is: ", p,"\n")
print("The generator is 14, a primitive root of p\n")
print("Bob and Alice's secret numbers are \"randomly\" selected from between 0 to 999\n")
a = compute_random()
b = compute_random()
bob = compute_shared(g,p,b)
alice = compute_shared(g,p,a)
alice_shared_secret = compute_shared(bob,p,a)
bob_shared_secret = compute_shared(alice,p,b)
if (alice_shared_secret == bob_shared_secret):
	print("This is Alice and Bob's Shared Secret:", alice_shared_secret, "\n")



#now we will try to "hack" this encryption
def hacky_hack_hack(alice, bob, real_answer):
	s=0
	a=1
	b=1
	time_start = time.time()
	while (s<=10):
		if(compute_shared(g,p,a) != alice):
			a += 1
			time.sleep(1)
			s= int(time.time() - time_start)
		else:
			print("Found Alice's secret key!")
			s = 0
			while (s<=10):
				if(compute_shared(g,p,b) != bob):
					b += 1
					time.sleep(1)
					s= int(time.time() - time_start)
				else:
					print("Found Bob's secret key!")
					if(compute_shared(compute_shared(g,p,a),p,b) == real_answer):
						print("Eve found the secret key!! We genuinely didn't see that one coming. Dumb luck I guess.")
						return real_answer

	print("The session has timed out")
	return 0

print("This is our attempt to hack the system")
print(hacky_hack_hack(alice, bob, alice_shared_secret))