largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done":
        break
    try: 
        num = int(num)
    except:
        print "Invalid input"
        continue
    if smallest is None:
    	smallest = num
    if num < smallest:
        smallest = num
    if largest is None:
    	largest = num
    if num > largest: 
    	largest = num 
print "Maximum is", largest
print "Minimum is", smallest