'''
import pandas as pd
import numpy as np
# Machine Learning Library
import sklearn.linear_model as skl_lm
# Plotting Library
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# read in data
advertising = pd.read_csv('Advertising.csv', usecols=[1,2,3,4])
advertising.info()

# extract predictors and response
X = advertising['TV'].values.reshape(-1,1)
y = advertising['sales']

# use the function that sklearn provides to do the LR
regr = skl_lm.LinearRegression()
regr.fit(X,y)

# obtain the model parameters
print(regr.intercept_) # => 7.032593549127693
print(regr.coef_)      # => [0.04753664]

# prediction based on LR parameters
y_pred = regr.intercept_ + regr.coef_* X
œ
# plot graph
plt.plot(X, y,'o',color='r')
plt.plot(X, y_pred, 'b', label="Prediction")
plt.legend()
plt.xlabel("TV")
plt.ylabel("sales")
plt.title('Regression: Sales ~ TV Advertising')
plt.show()
'''

import pandas as pd
import numpy as np
# Machine Learning Library
import sklearn.linear_model as skl_lm
# Plotting Library
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# read in data
advertising = pd.read_csv('Advertising.csv', usecols=[1,2,3,4])
advertising.info()

# extract predictors and response
X = advertising[['TV', 'radio']]
y = advertising.sales

# use the function that sklearn provides to do the LR
regr = skl_lm.LinearRegression()
regr.fit(X,y)

# obtain the model parameters
print(regr.intercept_) # => 2.9210999124051362
print(regr.coef_) # => [0.04575482 0.18799423]

# plot graph
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Use data-driven ranges with some padding
TV_min, TV_max = advertising['TV'].min(), advertising['TV'].max()
radio_min, radio_max = advertising['radio'].min(), advertising['radio'].max()

TV_range = np.linspace(TV_min, TV_max, 50)
radio_range = np.linspace(radio_min, radio_max, 50)
TV_ax, Radio_ax = np.meshgrid(TV_range, radio_range, indexing='xy')

# Calculate the predicted surface
Z = regr.intercept_ + TV_ax*regr.coef_[0] + Radio_ax*regr.coef_[1]

# Plot the surface
ax.plot_surface(TV_ax, Radio_ax, Z, alpha=0.4, color='blue', label='Regression Plane')

# Plot the actual data points
ax.scatter3D(advertising['TV'], advertising['radio'],
             advertising['sales'], c='r', s=50, label='Data Points')

ax.set_xlabel('TV')
ax.set_ylabel('Radio')
ax.set_zlabel('Sales')
plt.title('Regression: Sales ~ TV + Radio Advertising', fontsize=12)

plt.tight_layout()
plt.show()


