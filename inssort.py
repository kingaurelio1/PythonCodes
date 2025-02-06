def insSort(a):
	for j in range(1,len(a)):
		key = a[j]
		a[j]=key
		i = j-1
		while i >= 0 and a[i] > key:
			a[i+1]=a[i]
			i=i-1
		a[i+1]=key
	return a
print(insSort([6,5,2,1,3,4]))