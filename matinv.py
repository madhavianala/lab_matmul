def minv(a,b):
	if(a!=b):
		print("inverse of the matrix is not possible")
	else:
		A=[]
		ro=[]
		co=[]
		for i in range(0,a):
			ro += [0]
		for j in range(0,b):
			co += [0]
		for i in range(0,a):
			ro[i] = co
		A=ro
		print(A)
		for x in range(0,len(A)):
			for y in range(0,len(A[0])):
				A[x][y]=input("Enter elements for matrix:")
		print(A)
			
a=int(input("Enter number of rows for matrix:"))
b=int(input("Enter number of colunms for matrix:"))
minv(a,b)