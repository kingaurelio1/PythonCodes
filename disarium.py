def is_disarium(n):
	s=str(n)
	t=0
	u=True
	for i in range(len(s)):
		t+= int(s[i])**(i+1)
	if t == n:
		u=True
	else:
		u=False
	return u
num_vector, res_vector = [
  [6, 75, 135, 466, 372, 175, 1, 696, 876, 89, 518, 598],
  [True, False, True, False, False, True, True, False, False, True, True, True]
]
for i, n in enumerate(num_vector): Test.assert_equals(is_disarium(n), res_vector[i])