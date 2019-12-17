import math
import decimal
import random
import time
import os

#Thix is the Whole Algorithm
def compute_shared(g,p,k):
	return (g ** k ) % p

def compute_random():
	return random.randint(0,100)

def sophie_germain(p,n):
	for i in range(n):
		p = (2*p) + 1
	return p
p = sophie_germain(23,50) #computes a large prime number

print("The random prime number is: ")
print(p)
g = 5 # A primitive root of 23
a = compute_random()
b = compute_random()
bob = compute_shared(g,p,b)
alice = compute_shared(g,p,a)
alice_shared_secret = compute_shared(bob,p,a)
bob_shared_secret = compute_shared(alice,p,b)
if (alice_shared_secret == bob_shared_secret):
	print("This is Alice and Bob's Shared Secret:")
	print(alice_shared_secret)



#now we will try to "hack" this encryption
def hacky_hack_hack(alices_answer, real_answer):
	s=0
	time_start = time.time()
	while (s<=10):
		our_guess = alices_answer
		if (real_answer != our_guess):
			our_guess = our_guess + 1
			time.sleep(1)
			s= int(time.time() - time_start)

		else:
			return our_guess

#		s=s+1
#		return our_guess
	print("The session has timed out")
	return 0

print("This is our attempt to hack the system")
print(hacky_hack_hack(alice, alice_shared_secret))
# p = decimal.Decimal(2**1536 - 2**1472 - 1 + 2**64 * { decimal.Decimal[2**(1406*math.pi)] + 741804 })