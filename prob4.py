def palindrome():
	
	p = []
	s = range(100,1000)
	
	for i in s:
		for j in s:
			m = i * j
			var = str(m)
			if var [::-1] == var:
				p.append(m)
			
	return p

answer = max(palindrome())
print answer
