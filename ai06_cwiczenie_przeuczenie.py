# 1. Wczytaj zbiór danych przez "load_breast_cancer" z biblioteki scikit-learn
# 2. podziel zbiór na treningowy i testowy 60% - 40%, random_state=100
# 3. Wytrenuj model DecisionTreeClassifier -> wytrenuj z różnymi wartościami max_depth od 1 do 10
# 4. Określ optymalną głębokość drzewa w oparciu o score dla zbiorów treningowego i testowego
# ------------------------------------------------------
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

dane = datasets.load_breast_cancer()
cechy = dane.data
wyniki = dane.target

# Podział na trening/test
cechy_trening, cechy_test, wyniki_trening, wyniki_test = train_test_split(
    cechy, wyniki, test_size=0.4, random_state=100
)

model = KNeighborsClassifier(n_neighbors=5)
model.fit(cechy_trening, wyniki_trening)

wyniki_przewidywane = model.predict(cechy_test)

dokladnosc = accuracy_score(wyniki_test, wyniki_przewidywane)
print(f'Dokładność (accuracy): {dokladnosc}')

from sklearn.metrics import confusion_matrix, classification_report
# 1. Wygeneruj macierz pomyłek i wypisz ją
# 2. Wygeneruj raport klasyfikacyjny i wypisz
macierz_konf = confusion_matrix(wyniki_test, wyniki_przewidywane)
raport = classification_report(wyniki_test, wyniki_przewidywane, target_names=dane.target_names)
print('Macierz pomyłek:')
print(macierz_konf)
print('Raport klasyfikacji:')
print(raport)


