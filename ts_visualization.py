# A quick and dirty check to see if your time series is non-stationary
# is to review summary statistics


# from pandas import read_csv
# from matplotlib import pyplot
#
# series = read_csv('daily-total-female-births.csv', header=0, index_col=0)
# series.hist()
# pyplot.show()

# from pandas import read_csv
# series = read_csv('daily-total-female-births.csv', header=0, index_col=0)
# X = series.values
# print("Total dataset",len(X))
# split = round(len(X) / 2)
# print (split)
# X1, X2 = X[0:split], X[split:]
# # mean1=X1.mean()
# # mean2=X2.mean()
#
# mean1, mean2 = X1.mean(), X2.mean()
# var1, var2 = X1.var(), X2.var()
# print('mean1=%f, mean2=%f' % (mean1, mean2))
#
# print('variance1=%f, variance2=%f' % (var1, var2))

# from pandas import read_csv
# series = read_csv('airline-passengers.csv', header=0, index_col=0)
# X = series.values
# split = len(X) / 2
# X1, X2 = X[0:split], X[split:]
# mean1, mean2 = X1.mean(), X2.mean()
# var1, var2 = X1.var(), X2.var()
# print('mean1=%f, mean2=%f' % (mean1, mean2))
# print('variance1=%f, variance2=%f' % (var1, var2))

from pandas import read_csv
from matplotlib import pyplot
from numpy import log
series = read_csv('airline-passengers.csv', header=0, index_col=0)
X = series.values
X_log = log(X)

pyplot.hist(X)
pyplot.show()

pyplot.plot(X)
pyplot.show()

pyplot.hist(X_log)
pyplot.show()

pyplot.plot(X_log)
pyplot.show()