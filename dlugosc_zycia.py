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

