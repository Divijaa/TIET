import pandas as pd
import math

data=pd.read_csv(r'C:\Users\hp\Desktop\cs_data.csv')
data.head()

df=data.iloc[:,0:4]
print(df)

# data = data.drop(columns="sales")
# print(data)

#using karl pearson method to calculate VIF
def calculate(x1,x2):
    n = len(x1)
    sum_x1 = 0
    sum_sq_x1 = 0
    sum_x2 = 0
    sum_sq_x2 = 0
    sum_x1_x2=0
    


    for i in range(n):
        sum_x1 += x1[i]
        sum_sq_x1 +=(x1[i]*x1[i])
        sum_x2 += x2[i]
        sum_sq_x2 +=(x2[i]*x2[i])
        sum_x1_x2 +=x1[i]*x2[i]
        
        
        
    r=0
    num =0
    den= 0

    num = (n*sum_x1_x2) - (sum_x1*sum_x2)
    den = math.sqrt((n*sum_sq_x1)-(sum_x1**2))*math.sqrt((n*sum_sq_x2)-(sum_x2**2))

    r=num/den

    r_sq = r*r
    print('r_sq=', r_sq)
    
    vif=1/(1-r_sq)
    print('vif =' ,vif)

    for i in range(df.shape[1]):
        for j in range(i+1,df.shape[1]):
            calculate(df.iloc[:,i],df.iloc[:,j])

from statsmodels.stats.outliers_influence import variance_inflation_factor  
from statsmodels.tools.tools import add_constant       

vif = pd.DataFrame()
vif["features"] = df.columns
vif["VIF Factor"] = [variance_inflation_factor(df.values, i) 
                     for i in range(df.shape[1])]

print(vif)