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

for depth in range(1,11):
    model = DecisionTreeClassifier(max_depth=depth, random_state=100)
    model.fit(cechy_trening, wyniki_trening)

    # dla każdego max_depth zapamiętaj depth i poniższe parametry
    trening_dokladnosc = model.score(cechy_trening, wyniki_trening)
    test_dokladnosc = model.score(cechy_test, wyniki_test)

    print(f'{depth}: trening - {trening_dokladnosc:.4f} ; test - {test_dokladnosc:.4f}')

# wypisz wyniki / narysuj wykres



