hrs = raw_input("Enter Hours:")
rt = raw_input ("Enter rate:")
hrsfloat = float(hrs)
rtfloat = float (rt)
h = hrsfloat
r = rtfloat

def computepay(h,r):
    if h > 40:
        diff = h - 40
        finalpay = (40*r) + (r*1.5*diff)
        return finalpay
    else:
        finalpay = h*r
        return finalpay
    
    
p = computepay(h,r)
print p
