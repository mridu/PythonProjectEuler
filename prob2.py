def fib(n):		
	a, b = 1, 2
	sum = 0
	while b <= n:
		if b%2 == 0:
			sum += b
		print b,
		a, b = b, b+a
	return sum

num = int(raw_input("Enter limit: "))
answer = fib(num)
print "The sum of evens is :: %d" %answer