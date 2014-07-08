hrs = raw_input("Enter Hours:")
rate = raw_input("Enter rate:") 
h = float(hrs)
r = float(rate)
if h > 40:
    diff = h - 40
    finalpay = (40 * r) + (r*1.5*diff)
    print finalpay
else: 
	finalpay = h*r
	print finalpay
