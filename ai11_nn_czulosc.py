from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.metrics import accuracy_score

dane = fetch_openml(data_id=1466, as_frame=True, parser='auto')
cechy = dane.data # X
wyniki = dane.target # y

print('Cechy:')
print(cechy.describe())
print(cechy.head())

print('Wyniki:')
print(wyniki.head())

kfold = RepeatedStratifiedKFold(n_splits=3, n_repeats=2, random_state=100)

for indeksy_trening, indeksy_test in kfold.split(cechy, wyniki):
    cechy_trening, cechy_test = cechy.iloc[indeksy_trening,:], cechy.iloc[indeksy_test,:]
    wyniki_trening, wyniki_test = wyniki.iloc[indeksy_trening], wyniki.iloc[indeksy_test]

    model = MLPClassifier(random_state=100, hidden_layer_sizes=(50,), max_iter=2000)
    model.fit(cechy_trening, wyniki_trening)
    wyniki_pred = model.predict(cechy_test)
    dokladnosc = accuracy_score(wyniki_test, wyniki_pred)
    print(dokladnosc)



