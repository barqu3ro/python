from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf

real_diff_1 = real_diff_1.dropna()

fig, ax = plt.subplots(1,2,figsize=(10,5))
plot_acf(real_diff_1, lags=40, ax=ax[0])
plot_pacf(real_diff_1, lags=40, ax=ax[1])
plt.show()

adf_test = adfuller(real_diff_1)
print("The p-value: ", adf_test[1])