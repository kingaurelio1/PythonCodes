def id_mtrx(n):
	l=[]
	if type(n) is not int:
		return "Error"
	elif n==0:
		return []
	elif n>0:
		for i in range(n):
			w=[]
			for j in range(n):
				if i==j:
					w.append(1)
				else:
					w.append(0)
			l.append(w)
		return l
	else:
		for i in range(-n):
			a=[]
			for j in range(-n):
				if j==-n-1-i:
					a.append(1)
				else:
					a.append(0)
			l.append(a)
		return l
print(id_mtrx(-3))