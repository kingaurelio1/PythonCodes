import math
from collections import deque
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
def is_powerful(n):
	l=deque()
	s=0
	t=True
	if prime(n):
		return False
	else:
		for i in range(1,int(math.sqrt(n)+1)):
			if n%i==0 and prime(i):
				l.append(i)
	while l:
		key=l.popleft()
		if n%key**2==0:
			continue
		else:
			t=False
			break
	return t
print(is_powerful(64))