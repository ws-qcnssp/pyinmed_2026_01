# 1. Przygotowanie danych do analizy medycznej
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score
import numpy as np

dane = {
    'Wiek': [45, 62, 33, 70, 55, np.nan, 60, 39, 75, 29],
    'CRP': [5.1, 12.5, np.nan, 15.0, 7.2, 4.5, 11.1, 2.0, 18.3, 1.5],
    'Plec': ['K', 'M', 'K', 'M', 'K', 'M', 'K', 'K', 'M', 'M'],
    'Palenie': ['Tak', 'Nie', 'Nie', 'Tak', 'Nie', 'Tak', 'Nie', 'Nie', 'Tak', 'Nie'],
    'Wynik': [1, 1, 0, 1, 0, 1, 1, 0, 1, 0] # 1 = Podwyższone ryzyko, 0 = Niskie ryzyko
}

df = pd.DataFrame(dane)
print(df.info())
print(df.head())

cechy = df[['Wiek', 'CRP', 'Plec', 'Palenie']]
wyniki = df['Wynik']

# 2. Bez przygotowania - nie zadziała
# cechy_trening, cechy_test, wyniki_trening, wyniki_test = train_test_split(
#     cechy, wyniki, test_size=0.4, random_state=100
# )
# model.fit(cechy_trening, wyniki_trening)

# 3. One-Hot encoding
# ręcznie
# cechy['Plec_K'] = cechy['Plec'] == 'K'
# cechy['Plec_M'] = cechy['Plec'] == 'M'
# pandas
cechy_kodowane = pd.get_dummies(cechy, columns=['Plec', 'Palenie'], drop_first=True)
print(cechy_kodowane.head())

# 4. Podział na dane treningowe i testowe
cechy_trening, cechy_test, wyniki_trening, wyniki_test = train_test_split(
    cechy_kodowane, wyniki, test_size=0.4, random_state=42
)

# 5a. wprowadzenie brakujących danych
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy='mean')
cechy_trening[['Wiek', 'CRP']] = imputer.fit_transform(cechy_trening[['Wiek', 'CRP']])
cechy_test[['Wiek', 'CRP']] = imputer.transform(cechy_test[['Wiek', 'CRP']])

print(f'średnie użyte do uzupełnienia braków: {imputer.statistics_}')

# 5b. Standaryzacja kolumn numerycznych
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
cechy_trening[['Wiek', 'CRP']] = scaler.fit_transform(cechy_trening[['Wiek', 'CRP']])
cechy_test[['Wiek', 'CRP']] = scaler.transform(cechy_test[['Wiek', 'CRP']])

print(cechy_trening.head())
print(f'Min: {scaler.data_min_}, Max: {scaler.data_max_}')

# 6. trenowanie modelu
model = tree.DecisionTreeClassifier()

