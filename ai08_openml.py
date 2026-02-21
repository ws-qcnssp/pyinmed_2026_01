from sklearn.datasets import fetch_openml
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from  sklearn.ensemble import RandomForestClassifier

dane = fetch_openml(data_id=1506, as_frame=True, parser='auto')
cechy = dane.data
wyniki = dane.target

print(cechy.head())
print(cechy.info())

cechy_num = cechy.select_dtypes(include=['int64', 'float64']).columns
print(cechy_num)
cechy_kat = cechy.select_dtypes(include=['object', 'category']).columns
print(cechy_kat)

num_transformer = Pipeline(
    steps=[
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler())
    ]
)

kat_transformer = Pipeline(
    steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value='brak')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ]
)

preprocesor = ColumnTransformer(
    transformers=[
        ('num', num_transformer, cechy_num),
        ('cat', kat_transformer, cechy_kat),
    ]
)

model_pipeline = Pipeline(
    steps=[
        ('preprocessor', preprocesor),
        ('classifier', RandomForestClassifier(max_depth=5, random_state=100))
    ]
)

