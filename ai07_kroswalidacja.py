# 1. Wczytaj zbiór danych przez "load_breast_cancer" z biblioteki scikit-learn
# 2. podziel zbiór na treningowy i testowy 60% - 40%, random_state=100
# 3. Wytrenuj model DecisionTreeClassifier -> wytrenuj z różnymi wartościami max_depth od 1 do 10
# 4. Określ optymalną głębokość drzewa w oparciu o score dla zbiorów treningowego i testowego
# ------------------------------------------------------
from sklearn import datasets
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pandas as pd

dane = datasets.load_breast_cancer()
cechy = dane.data
wyniki = dane.target

# Podział na trening/test
cechy_trening, cechy_test, wyniki_trening, wyniki_test = train_test_split(
    cechy, wyniki, test_size=0.2, random_state=100
)

model = DecisionTreeClassifier(random_state=100)
# model.fit(cechy_trening, wyniki_trening)

parametry = {'max_depth': [2,3,4,6,8], 'min_samples_leaf': [1,3,5]}
walidator = GridSearchCV(model, parametry, cv=3)
walidator.fit(cechy_trening, wyniki_trening)
print(f'Najlepsze parametry: {walidator.best_params_}')
print(f'Najlepsza dokładność: {walidator.best_score_}')

wyniki_kros = pd.DataFrame(walidator.cv_results_)
print(wyniki_kros.head())




