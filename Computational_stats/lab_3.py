import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("headbrain.csv")

#head size is independent
#brain weight is dependent

#values() returns a list of all the values available in given data
x = data['Head Size(cm^3)'].values
y = data['Brain Weight(grams)'].values
print(data.head())

#237 input values
# total no.of input values
l = len(x)

sum_x =0
sum_y =0

# calculating the mean of x and y
for i in range(l):
    sum_x += x[i]
    
mean_x = sum_x/l

for i in range(l):
    sum_y += y[i]
    
mean_y = sum_y/l

# using the formula to calculate m & c

numer = 0
denom = 0
for i in range(l):
    
    numer += (x[i] - mean_x) * (y[i] - mean_y)
    denom += (x[i] - mean_x) ** 2
    
m = numer / denom
c = mean_y - (m * mean_x)

print('The value of m =' ,m)
print('The value of c =' ,c)

#m is b1 and c is b0
# y=b0 +b1*x

y_reg=[]
y_reg= c+(m*x)

plt.figure(figsize =(10,8))

plt.scatter(x,y, color ="green" ,label ="plot of head size v/s brain weight")
plt.plot(x,y_reg ,color ="red" , label ="regression line")

plt.xlabel("Head Size")
plt.ylabel("Brain Weight")
plt.legend()

plt.title("Plot of linear Regression")
plt.show()

from sklearn.linear_model import LinearRegression
Reg_model = LinearRegression()
x=np.array(x)
y=np.array(y)

#array will get reshaped in such a way that the resulting array has only 1 column
#no reshaping,error while fitting it in the model.
x=x.reshape(-1,1)
y=y.reshape(-1,1)

#takes array as an input
Reg_model.fit(x,y)

Reg_model.coef_

Reg_model.intercept_

# calculating R-squared value for measuring goodness of our model. 

ss_t = 0 #total sum of squares
ss_r = 0 #total sum of square of residuals

for i in range(len(x)):
    
    y_pred = c + m * x[i]
    ss_t += (y[i] - mean_y) ** 2
    ss_r += (y[i] - y_pred) ** 2
    
r2 = 1 - (ss_r/ss_t)

print(r2)