r1=input("no.of rows in m1=")
c1=input("no.of colums in m1=")
r2=input("no.of rows in m2=")
c2=input("no.of colums in m2=")
if(c1==r2):
	i=0
	x={}
	while(i<r1):
		j=0
		while(j<c1):
			m1=input("enter elements of m1=")
			x[i,j]=m1
			j=j+1
		i=i+1
	i=0
	y={}
	while(i<r2):
		j=0
		while(j<c2):
			m2=input("enter elements of m2=")
			y[i,j]=m2
			j=j+1
		i=i+1
	i=0
	z={}
	while(i<r1):
		j=0
		while(j<c2):
			z[i,j]=0
			k=0
			while(k<c2):
				z[i,j]=z[i,j]+x[i,k]*y[k,j]
				k=k+1
			j=j+1
		i=i+1
	i=0
	while(i<r1):
		j=0
		while(j<c2):
			print z[i,j]
			j=j+1
		i=i+1
else:
   print "multiplication is not possible"
        



