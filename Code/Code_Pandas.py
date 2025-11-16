import numpy as np
import pandas as pd
# At default, Series is just like 1-D Numpy array
data = pd.Series([0.25,0.5,0.75,1])
data[0] # => 0.25
data[1:3] # => [0.5, 0.75]

# Series as a generalized Numpy array. 
# It allows arbitrary indexing, not only integers
data = pd.Series([0.25, 0.5, 0.75, 1.0],index=['a', 'b', 'c', 'd'])
data['a'] # => 0.25
data['b':'d'] # => [0.5, 0.75, 1.0]

''' Suppose we have sales data on two products (milk and coke)
over three months (Jan ~ Mar) as follow. There are 3 methods to 
create a DataFrame representing the sales data.'''
data = np.array([[11,13],
                 [5,6],
                 [1,2]])
# Method 1: Specify data, index and columns simultaneously 
df1 = pd.DataFrame(data, index = ['Jan','Feb','Mar'], columns = ['Milk','Coke'])

# Method 2: First use Dictionary to link columns with data, then add index
data_dict = {'Milk':[11,5,1], 'Coke':[13,6,2]}
df2 = pd.DataFrame(data_dict, index = ['Jan','Feb','Mar'])

# Method 3: First specify index and columns, then add data
df3 = pd.DataFrame(index = ['Jan','Feb','Mar'], columns = ['Milk','Coke'])
df3['Milk'] = data[:,0]
df3['Coke'] = data[:,1]


# read in data and store it in a dataframe
advertising = pd.read_csv('Advertising.csv',
                          usecols=[1,2,3,4])
# print out first few rows of the dataframe
advertising.head()
# print out information about the dataframe
advertising.info()

