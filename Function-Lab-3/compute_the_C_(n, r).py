# WAP to compute the C (n, r) using the user defined function. 

def nCr(n, r): 
	return (fact(n) / (fact(r) 
				* fact(n - r))) 
def fact(n): 
	res = 1
	for i in range(2, n+1): 
		res = res * i 
	return res 
n = int(input("Enter val n: "))
r = int(input("Enter val r: "))
print(int(nCr(n, r))) 


# Working on this!