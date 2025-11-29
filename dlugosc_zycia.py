import pandas as pd

df = pd.read_csv('data.csv')

# kolumna Dim1 -> płeć
dff = df[['Indicator', 'Location', 'Dim1', 'Period', 'FactValueNumeric']]