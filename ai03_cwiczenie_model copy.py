# 1. Wczytaj zbiór danych przez "load_breast_cancer" z biblioteki scikit-learn
# 2. podziel zbiór na treningowy i testowy 75% - 25%, random_state=100
# 3. Wytrenuj model KNN (KNeighborsClassifier) z n_neighbors=5 (poszukaj w dokumentacji scikit-learn / Google)
# 4. Oceń dokładność modelu (accuracy)
# ------------------------------------------------------
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

dane = datasets.load_breast_cancer()
cechy = dane.data
wyniki = dane.target

# Podział na trening/test
cechy_trening, cechy_test, wyniki_trening, wyniki_test = train_test_split(
    cechy, wyniki, test_size=0.25, random_state=100
)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(cechy_trening, wyniki_trening)

wyniki_przewidywane = model.predict(cechy_test)

dokladnosc = accuracy_score(wyniki_test, wyniki_przewidywane)
print(f'Dokładność (accuracy): {dokladnosc}')

