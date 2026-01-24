# 1. wczytanie danych - gotowe dane z biblioteki scikit-learn - load_iris
from sklearn.datasets import load_iris
dane_iris = load_iris()

# 2. Analiza danych
print(f'Cechy w zbiorze: {dane_iris.feature_names}')
print(f'Kategorie w zbiorze: {dane_iris.target_names}')
