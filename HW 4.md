**HW 4**

**Requirements** 

Use the provided dataset smarket.csv, where the first two columns are indices and not used as predictors. Predict whether the market will go UP or Down (Direction) based on the historical information on 6 features: Lag1-Lag5 & Volume (Note: Year Value should not be used for fitting and Today Value is used to determine direction). 2. Use data with Year < 2005 for training and Year = 2005 for testing. 3. Submit a single **“.ipynb” file containing Python code that clearly displays the results for each assignments.**

**How to run the notebook**

1. Install the dependencies (Jupyter plus numpy/pandas/matplotlib are already included in the base Anaconda distribution):

   ```bash
   pip install notebook numpy pandas matplotlib
   ```

2. Start Jupyter in this folder and open `HW4_Assignment1.ipynb`:

   ```bash
   jupyter notebook
   ```

   (Alternatively, execute it non-interactively with `jupyter nbconvert --to notebook --execute HW4_Assignment1.ipynb`).

3. From the Notebook menu, choose **Kernel → Restart & Run All** to execute every cell in order. The final cell prints the testing accuracy for the logistic regression model.

 

 **Assignments**

1. Fit a logistic regression (LR) model using Lag1-Lag5 & Volume, and print out classification accuracy on testing data. 
2. Fit a logistic regression (LR) model using Lag1 and Lag2 only, i) print out accuracy; ii) compare its accuracy with Assignment 1 and discuss which performs better and why. 
3. Apply Linear Discriminant Analysis (LDA) using Lag1 and Lag2 only, i) plot the Receiver operating characteristic (ROC) curve for the classifier; ii) compute the Area Under the Curve (AUC). 
4. Apply Quadratic Discriminant Analysis (QDA) using Lag1 and Lag2 only, i) plot the ROC curve for the classifier; ii) compute the AUC; iii) compare its results with LDA in Assignment 3 and discuss which performs better and why.

 

Hint: You may find the following packages useful for data processing and model fitting (use pip to install them if needed)

Numpy

Pandas

Statsmodels.api.Logit 

Sklearn.discriminant_analysis.LinearDiscriminantAnalysis

Sklearn.discriminant_analysis.QuadraticDiscriminantAnalysis

Sklearn.metrics.accuracy_score & confusion_matrix 

Seaborn 

Matplotlib 

Alternatively, feel free to use other packages or write your own functions when needed