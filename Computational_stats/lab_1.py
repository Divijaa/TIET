import numpy as np
import pandas as pd

import statistics
import math



#random.randit is used to generate random numbers in a particular range
data = np.random.randint(0, 100, size=(5, 3))

#pd.dataframe prints data in tabular form ,thus easy to access
df = pd.DataFrame(data, columns=['random_1', 'random_2', 'random_3'])
print(df)

#iloc helps to extract rows and col to make x array
x=df.iloc[:,:].values

#.shape gives the dimensions of the dataframe
print(x.shape)

n=x.shape[0]
m=x.shape[1]

#for harmonic mean

sumh=0
for i in range(n):
    sumh=sumh+1/x[i][0]
        
hm=(n)/sumh
print('harmonic mean by formula is :', round(hm, 2))
print('harmonic mean by inbuilt function is :' ,round(statistics.harmonic_mean(df.random_1), 2))




#for geometric mean

product=1
for i in range(n):
    product=product * x[i][0]
    
gm = (float)(math.pow(product, (1 / n)))
print('geometeric mean by formula is :', round(gm, 2))
print('geometeric mean by inbuilt function is :' ,round(statistics.geometric_mean(df.random_1), 2))




#for mean of data

sum =0
for i in range(n):
    for j in range(m):
        sum=sum+x[i][j]
me=sum/(n*m)  
print('mean by formula is :', round(me, 2))
print('mean by inbuilt function is :' ,round(np.mean(x), 2))







#for median of data

#first we have to sort the data
a=np.array(x)
def sortRowWise(a):
    # One by one sort individual rows.
    for i in range(len(a)):
        a[i].sort()
    return 0

MAX = 100; 
# Function to find median in the matrix
def median_using_binary(a, n, m):
    mi = a[0][0]
    mx = 0
    for i in range(n):
        #finding min
        if a[i][0] < mi:
            mi = a[i][0]
        #finding max
        if a[i][m-1] > mx :
            mx =  a[i][m-1]
     
     #stores the value of median if matrix is put in array format
    desired = (n * m + 1) // 2
     
    while (mi < mx):
        mid = mi + (mx - mi) // 2
        #place stores the number of elements less than mid in the matrix
        place = [0];
         
        # Find count of elements smaller than mid
        for i in range(n):
             j = upper_bound(a[i], mid)
             place[0] = place[0] + j
        if place[0] < desired:
            mi = mid + 1
        else:
            mx = mid
    return mi
    
#calling of functions 
sortRowWise(a)
mi=median_using_binary(a, n, m)


print ("Median by formula is", mi)
print('median by inbuilt function is :' ,round(np.median(x), 2))
var=0
for i in range(n):
    for j in range(m):
        var=var+(x[i][j]-sum/(n*m))**2






#for variance

print('variance by inbuilt function is',round(np.var(x),2))
def variance(a, n, m, me):
    sum1 = 0;
    for i in range(n):
        for j in range(m):
 
            # subtracting mean from elements
            a[i][j] -= me;
 
            # squaring each terms
            a[i][j] *= a[i][j];
 
    # taking sum
    for i in range(n):
        for j in range(m):
            sum1 += a[i][j];

    return sum1/(n*m)
variance(x,n,m,me)
print('variance by formula is', round(var/(n*m),2))