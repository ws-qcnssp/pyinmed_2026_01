from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import RepeatedStratifiedKFold

dane = fetch_openml(data_id=1466, as_frame=True, parser='auto')
cechy = dane.data # X
wyniki = dane.target # y

print('Cechy:')
print(cechy.describe())
print(cechy.head())

print('Wyniki:')
print(wyniki.head())

