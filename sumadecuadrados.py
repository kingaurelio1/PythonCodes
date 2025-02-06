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
def squares_sum(n):
	w=False
	u=[]
	if prime(n):
		if n%4 != 3:
			w=True
	else:
		for i in range(math.sqrt(n)+1):
			if n%i==0 and prime(i):
				u.append(i)
		for j in u:
			if j%4==3: