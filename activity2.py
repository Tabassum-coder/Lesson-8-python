num=int(input("Enter numerator"))
den=int(input("Enter denominator"))

if num%den==0:
    print("{0} is divisible by {1}".format(num,den))
else:
    print("{0} is not divisible by {1}".format(num,den))