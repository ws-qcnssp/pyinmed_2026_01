# 1. wczytanie danych - gotowe dane z biblioteki scikit-learn - load_iris
from sklearn.datasets import load_iris
dane_iris = load_iris()
dane_ramka = load_iris(as_frame=True)

# 2. Analiza danych
print(f'Cechy w zbiorze: {dane_iris.feature_names}')
print(f'Kategorie w zbiorze: {dane_iris.target_names}')
cechy = dane_iris.data
wyniki = dane_iris.target

print(f'Kształt cechy: {cechy.shape}')
print(f'Kształt wyniki: {wyniki.shape}')

print(wyniki)

# 3. Podział danych na zbiory treningowy i testowy - 70% danych -> trening, 30% -> test
from sklearn.model_selection import train_test_split
cechy_trening, cechy_test, wyniki_trening, wyniki_test = train_test_split(cechy, wyniki, test_size=0.3, random_state=100)

print(wyniki_test)

# 4. Budowa modelu do klasyfikacji
from sklearn import tree
model = tree.DecisionTreeClassifier()

# 5. Uczenie modelu na danych treningowych - metoda "fit"
model.fit(cechy_trening, wyniki_trening)
print('Model został nauczony')

