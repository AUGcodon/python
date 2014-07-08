grade = raw_input("What is your test score?")
intgrade = float(grade)
if intgrade >= 0.9:
    print "A"
elif intgrade >= 0.8:
	print "B"
elif intgrade >= 0.7:
	print "C"
elif intgrade >= 0.6:
    print "D"
elif intgrade < 0.6:
	print "F"