import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv(r'C:\Users\hp\Desktop\Iris.csv')
print(df.head(5))


def simpleline():
    #straight line graph
    plt.title('Linear graph')
    x = np.linspace(0, 10, 50)
    y=np.linspace(0, 5, 50)
    plt.plot(x,"o",y,"r")
    plt.xlabel('x-axis')
    plt.ylabel('Y-axis')
    plt.show()


def trigno():
    x= np.linspace(0,10,50)
    y= np.linspace(0,5,50)
    sin_x = np.sin(x)
    cos_y =np.cos(y)
    z=sin_x + cos_y
    w=sin_x**2
    plt.title('Trignometry')
    plt.plot(z,label ='z=sin_x+cos_y',color ='green',linestyle ='-')
    plt.plot(sin_x, label='sinwave', color ='red', linestyle = '--')
    plt.plot(cos_y, label='coswave', color ='blue', linestyle = '-')
    plt.plot(w, label='sin_x**2', color ='yellow', linestyle = '-')

    plt.legend()
    plt.show()


def subplots():
    names = ['group_1', 'group_2', 'group_3']
    values = [10, 50, 200]

    plt.figure(figsize=(10, 3))

    #bar-graph
    # 1x3 grid for 1st plot
    plt.subplot(131)
    plt.bar(names, values)

    #scatter plot
    plt.subplot(132)
    plt.scatter(names, values,c=['red'])

    #normal plot
    plt.subplot(133)
    plt.plot(names, values,"g",)


    plt.suptitle('Categorical Plotting')
    plt.show()


def symbols():
    #plot using diff symbols
    #arrange takes values start,stop and step 
    t = np.arange(0, 5, 0.2)

    plt.plot(t, t, 'g--', label='linear' )
    plt.plot(t, t**2, 'rs',label='square')
    plt.plot(t, t**3, 'b^',label='cube')
    plt.legend()
    plt.show()


def random_data():
    data1 = np.random.randn(2, 10)
    print(data1)
    print(data1.shape)
    plt.plot(data1)
    plt.show()


def pie_chart():
    species = ['SETOSA', 'VERSICOlOR', 'VIRGINIA']
  
    data = [50,50,50]
  
    # Creating plot

    fig = plt.figure(figsize =(10, 7))
    plt.pie(data, labels = species)
    plt.title('Different species of Irirs')
  
    # show plot
    plt.show()


def scatterplot_fileread():
    print('Enter any two attributes of the data(SepalWidthCm,SepalLengthCm ,PetalLengthCm,PetalWidthCm )')
    atr1=input()
    atr2=input()
    colors = {'Iris-setosa':'r', 'Iris-virginica':'g', 'Iris-versicolor':'y'}
    if atr1 == 'SepalWidthCm' and atr2 == 'SepalLengthCm' :
        plt.xlabel('SepalWidthCm')
        plt.ylabel('SepalLengthCm')
        plt.scatter(df.SepalWidthCm, df.SepalLengthCm, c=df['Species'].apply(lambda col_vector: colors[col_vector]), s = 100)
    elif atr1 == 'SepalWidthCm' and atr2 == 'PetalLengthCm' :
        plt.xlabel('SepalWidthCm')
        plt.ylabel('PetalLengthCm')
        plt.scatter(df.SepalWidthCm, df.PetalLengthCm, c=df['Species'].apply(lambda col_vector: colors[col_vector]), s = 100)
    elif atr1 =='PetalWidthCm' and atr2 == 'PetalLengthCm' :
        plt.xlabel('PetalWidthCm')
        plt.ylabel('PetalLengthCm')
        plt.scatter(df.PetalWidthCm, df.PetalLengthCm, c=df['Species'].apply(lambda col_vector: colors[col_vector]), s = 100)
    elif atr1 == 'PetalWidthCm' and atr2 =='SepalLengthCm' :
        plt.xlabel('PetalWidthCm')
        plt.ylabel('SepalLengthCm')
        plt.scatter(df.PetalWidthCm, df.SepalLengthCm, c=df['Species'].apply(lambda col_vector: colors[col_vector]), s = 100)

print("\n------------------------------------------------\n") 
print('1 Simpleline')
print('2 Trigno_functions')
print('3 Subplots')
print('4 Random_data_plot')
print('5 pie chart')
print('6 scatterplot_fileread')
print("\n------------------------------------------------\n") 

x=int(input("Enter your choice: "))

if x==1:
    simpleline()
    
elif x==2:
    trigno()
    
elif x==3:
    subplots()
    
elif x==4:
    random_data()
    
elif x==5:
    pie_chart()
    
elif x==6:
    scatterplot_fileread()
    
else:
    print("Please enter valid choice")