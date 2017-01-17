
from datalib import *
import pandas
import statsmodels.formula.api as sm
import os

# crime_1000,pop,income,perc_white,perc_black,perc_asian
OUT_PATH = "../plots"


if __name__=='__main__':

	data = pandas.read_csv(os.path.join(OUT_PATH, 'python_reg_regression.csv'))
	model = sm.ols(formula='reg ~ + age + income + college + unemp + white + black + asian + hisp + pop', data=data).fit()
	print(model.summary())
