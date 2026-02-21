from sklearn.datasets import fetch_openml
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from  sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

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

cechy_trening, cechy_test, wyniki_trening, wyniki_test = train_test_split(
    cechy, wyniki, test_size=0.2, random_state=100
)

model_pipeline.fit(cechy_trening, wyniki_trening)
wyniki_pred = model_pipeline.predict(cechy_test)
from sklearn.metrics import classification_report
print(classification_report(wyniki_test, wyniki_pred))