def toBinary(n):
	if n == 0:
		return "0"
	if n==1:
		return "1"
	if (n%2) ==0:
		return toBinary(n/2) + "0"
	return toBinary(n/2) + "1"

def toDecimal(b):
	return toDecimalIter(b,0)

def toDecimalIter(b,placeValue):
	if len(b)==0 : 
		return 0
	return ((2 ** placeValue)* int(b[-1])) + toDecimalIter(b[:-1], placeValue+1) 

def binaryReverse(n):
	binary = toBinary(n)
	reverse = binary[::-1]
	return toDecimal(reverse);

print binaryReverse(13)