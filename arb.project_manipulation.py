import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from scipy import stats

df = pd.read_excel('arb.project_clean_data.xlsx', sheet_name='sheet -> I')
print(df)

avg=round((df["price_m2"].mean()),0)
print(avg)
# print(df["price"].describe())
# print(df["area m2"].describe())
# print(df["price_m2"].describe())

#####
# linear regression of price and total area of house

x = list(df["price"])
y = list(df["area m2"])

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(str(round(r,3)) + " დამოკიდებულების კოეფიციენტი")

def myfunc(x):
  return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.show()

# # price dependency over state (bars)

# avg_old = []
# avg_new = []
# avg_black = []
# for i in df.index:
#     if df.loc[i, "state"] == "ძველი გარემონტებული" :
#         avg_old.append(df.loc[i, "price_m2"])
#     if df.loc[i, "state"] == "ახალი გარემონტებული" :
#         avg_new.append(df.loc[i, "price_m2"])
#     if df.loc[i, "state"] == "შავი კარკასი" :
#         avg_black.append(df.loc[i, "price_m2"])
#
# avg_old_i = sum(avg_old)/len(avg_old)
# avg_new_i = sum(avg_new)/len(avg_new)
# avg_black_i = sum(avg_black)/len(avg_black)
#
# x = np.array(["ახალი გარემონტებული", "ძველი გარემონტებული", "შავი კარკასი"])
# y = np.array([avg_new_i, avg_old_i, avg_black_i])
#
# plt.bar(x, y, color = "#4CAF50")
# plt.show()

# # multiple regression

# from sklearn import linear_model
# X = df[['rooms', 'area m2']]
# y = df['price']
#
# regr = linear_model.LinearRegression()
# regr.fit(X, y)
#
# print(regr.coef_)
#
# predictedPrice = regr.predict([[2, 50]])
# print(predictedPrice)
# predictedPrice1 = regr.predict([[3, 70]])
# print(predictedPrice1)
# predictedPrice2 = regr.predict([[2, 100]])
# print(predictedPrice2)
# predictedPrice3 = regr.predict([[5, 300]])
# print(predictedPrice3)
# predictedPrice4 = regr.predict([[3, 60]])
# print(predictedPrice4)
