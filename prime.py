import math
def prime(n):
	s = True
	t=2
	if n==1:
		s= False
	elif n==2 :
		s = True
	elif n%2==0:
		s=False
	else:
		while t < int(math.sqrt(n))+1:
			if n%t==0:
				s=False
				break
			t += 1
	return s
print(prime(3))   # True
print(prime(4))   # False
print(prime(17))  # True
print(prime(18))  # False