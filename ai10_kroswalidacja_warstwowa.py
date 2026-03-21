import pandas as pd

dane = {
    'Wiek': [45, 62, 33, 70, 55, 35, 60, 39, 75, 29],
    'CRP': [5.1, 12.5, 18, 15.0, 7.2, 4.5, 11.1, 2.0, 18.3, 1.5],
    'Plec': ['K', 'M', 'K', 'M', 'K', 'M', 'K', 'K', 'M', 'M'],
    'Palenie': ['Tak', 'Nie', 'Nie', 'Tak', 'Nie', 'Tak', 'Nie', 'Nie', 'Tak', 'Nie'],
    'Wynik': [1, 1, 0, 1, 0, 1, 1, 0, 1, 0] # 1 = Podwyższone ryzyko, 0 = Niskie ryzyko
}

df = pd.DataFrame(dane)

cechy = df[['Wiek', 'CRP', 'Plec', 'Palenie']]
wyniki = df['Wynik']

from sklearn.model_selection import RepeatedStratifiedKFold

