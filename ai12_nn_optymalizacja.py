from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
# from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.pipeline import Pipeline

# Wczytanie danych z OpenML - badania ILPD
dane = fetch_openml(data_id=1480, as_frame=True, parser='auto')
cechy = dane.data # X
wyniki = dane.target # y

print('Cechy:')
print(cechy.describe())
print(cechy.head())

print('Wyniki:')
print(wyniki.head())

cechy = pd.get_dummies(cechy, columns=['V2'], drop_first=True)
print(cechy.head())

pipeline = Pipeline([
    ('scaler', MinMaxScaler()),
    ('mlp', MLPClassifier(hidden_layer_sizes=(50), random_state=100, max_iter=5000))
])