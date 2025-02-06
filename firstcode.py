def is_harshad(n):
	s=0
	u=False
	t=str(n)
	for i in range(len(t)):
		s += int(t[i])
	if n%s==0:
		u=True
	else:
		u=False
	return u
print(is_harshad(171))