
sum = 0
for count in range (1,1000):
	if count%3 == 0 or count%5 == 0:
		#print "count = %r" % count
		sum += count
		#print "sum = %r" % sum

print "total = %r" % sum