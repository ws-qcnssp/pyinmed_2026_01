import pandas as pd
import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit

df = pd.read_csv('data.csv')

# kolumna Dim1 -> płeć
dff = df[['Indicator', 'Location', 'Dim1', 'Period', 'FactValueNumeric']]

# maska = dff['Indicator'] == 'Life expectancy at birth (years)'
# dff[dff['Indicator'] == 'Life expectancy at birth (years)']
dff = dff.query('Indicator == "Life expectancy at birth (years)" & Location == "Poland"')
dff_m = dff.query('Dim1 == "Male"')
dff_k = dff.query('Dim1 == "Female"')

c_m, b_m, a_m = polyfit(dff_m['Period'], dff_m['FactValueNumeric'], 2)
c_k, b_k, a_k = polyfit(dff_k['Period'], dff_k['FactValueNumeric'], 2)

plt.scatter(dff_m['Period'], dff_m['FactValueNumeric'], color='blue', label='mężczyźni')
plt.scatter(dff_k['Period'], dff_k['FactValueNumeric'], color='red', label='kobiety')

# f(x) = a*x^2 + b*x + c
plt.plot(dff_m['Period'], a_m * dff_m['Period'] ** 2 + b_m * dff_m['Period'] + c_m, color='blue', label='trend - M')
plt.plot(dff_k['Period'], a_k * dff_k['Period'] ** 2 + b_k * dff_k['Period'] + c_k, color='red', label='trend - k')

plt.legend()

# plt.savefig('wykres.png')
plt.show()