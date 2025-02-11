def box_seq(step):
	s=0
	if step == 0:
		return 0
	else:
		while step >0:
			if step%2==1:
				s+=3
			else:
				s-=1
			step-=1
		return s
