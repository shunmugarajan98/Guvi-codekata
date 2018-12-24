num=input()
num=[int(x) for x in num.split(',')]
rep = [x for n, x in enumerate(num) if x in num[:n]]
if(len(rep)==0):
	print ("Unique")
else:
	x =sorted(rep)
	print (x)
