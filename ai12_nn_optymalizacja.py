from sklearn.datasets import fetch_openml
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
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

hiperparametry = {
    'mlp__hidden_layer_sizes': [(100), (50), (50, 25), (30, 20, 10)],
    'mlp__activation': ['relu', 'tanh'],
    'mlp__solver': ['adam', 'sgd']
}

print('Grid search dla sieci MLP')
grid = GridSearchCV(pipeline, hiperparametry, cv=3, n_jobs=-1, scoring='accuracy')
grid.fit(cechy, wyniki)

print('Najlepszy wynik:')
print(f'parametry: {grid.best_params_}, dokładność: {grid.best_score_}')

print('Najlepsze wyniki całego grid search:')
wyniki_df = pd.DataFrame(grid.cv_results_)
wyniki_df = wyniki_df.sort_values(by='mean_test_score', ascending=False)
print(wyniki_df['param_mlp__hidden_layer_sizes', 'param_mlp__activation', 'param_mlp__solver', 'mean_test_score'].head())


