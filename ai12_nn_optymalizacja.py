from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
# from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV

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
    ('mlp', MLPClassifier(random_state=100, max_iter=5000))
])

# parametry = {'max_depth': [2,3,4,6,8], 'min_samples_leaf': [1,3,5]}
# walidator = GridSearchCV(model, parametry, cv=3)
hiperparametry = {
    'mlp__hidden_layer_sizes': [(100), (50), (50, 25), (30, 20, 10)],
    'mlp__activation': ['relu', 'tanh'],
    'mlp__solver': ['adam', 'sgd']
}

print('Grid search dla sieci MLP')
grid = GridSearchCV(pipeline, hiperparametry, cv=3, n_jobs=-1)

