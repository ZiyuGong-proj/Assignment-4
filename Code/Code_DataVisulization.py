import pandas as pd
# seaborn is a Library for data visualization
import seaborn as sns
# matplotlib is a Library for figure producing
import matplotlib.pyplot as plt

# read in the data and get a sense of it
data = pd.read_csv('smarket.csv',index_col=0)
data.head()
data.info()

# see the correlation between different predictors
corr = data.corr(numeric_only=True)
plt.figure(figsize = (8,8))
sns.heatmap(corr)

# plot 'Volume' against index
plt.figure(figsize = (12,6))
sns.scatterplot(x=data.index, y=data['Volume'])


plt.show()


