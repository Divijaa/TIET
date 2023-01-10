import pandas as pd
import math
import numpy as np

data=pd.read_csv(r'C:\Users\hp\Desktop\cs_data.csv')
data.head(3)

df=data.iloc[:,0:4]
X = df.to_numpy()
print(len(X))

ALL_ONE=[1]*len(X)

X=np.insert(X,0,ALL_ONE,axis=1)
print(X)

y=data.iloc[:,4]
Y=y.to_numpy()

X_T = X.T
print(X_T.shape[0])

X_mul = np.matmul(X_T,X)
print(X_mul.shape[0])
print(X_mul.shape[1])

X_inv = np.linalg.inv(X_mul)
print(X_inv)
print(X_inv.shape[0])
print(X_inv.shape[1])

X_final = np.matmul(X_inv, X_T)
# print(X_final)
Y_final= np.matmul(X_T,Y)
print(np.matmul(X_T,Y))

b=np.matmul(X_inv,Y_final)
c=np.matmul(X_final,Y)
print(b.shape)

print(b)
print(c)

Y_pred = []
for i in range(len(Y)):
    Y_pred+= [b[0] + b[1]*df.iloc[:,0][i] + b[2]*df.iloc[:,1][i] + b[3]*df.iloc[:,2][i] + b[4]*df.iloc[:,3][i]]
print(Y_pred)

e=0
for i in range(len(Y)):
    print((Y[i]-Y_pred[i])**2)
    e+=(Y[i]-Y_pred[i])**2
    
print(e)
print(e/len(Y))