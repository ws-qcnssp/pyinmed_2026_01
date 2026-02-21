# 1. Przygotowanie danych do analizy medycznej
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score

dane = {
    'Wiek': [45, 62, 33, 70, 55, 48, 60, 39, 75, 29],
    'CRP': [5.1, 12.5, 1.8, 15.0, 7.2, 4.5, 11.1, 2.0, 18.3, 1.5],
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

cechy['Plec_K'] = cechy['Plec'] == 'K'
print(cechy.head())

# model = tree.DecisionTreeClassifier()

# test

