import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# kolumna Dim1 -> płeć
dff = df[['Indicator', 'Location', 'Dim1', 'Period', 'FactValueNumeric']]

# maska = dff['Indicator'] == 'Life expectancy at birth (years)'
# dff[dff['Indicator'] == 'Life expectancy at birth (years)']
dff = dff.query('Indicator == "Life expectancy at birth (years)" & Location == "Poland"')
dff_m = dff.query('Dim1 == "Male"')
dff_k = dff.query('Dim1 == "Female"')

plt.scatter(dff_m['Period'], dff_m['FactValueNumeric'], color='blue', label='mężczyźni')
plt.scatter(dff_k['Period'], dff_k['FactValueNumeric'], color='red', label='kobiety')
plt.legend()

# plt.savefig('wykres.png')
# plt.show()