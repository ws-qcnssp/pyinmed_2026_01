from sklearn.datasets import fetch_openml

dane = fetch_openml(data_id=1466, as_frame=True, parser='auto')
cechy = dane.data # X
wyniki = dane.target # y

print(cechy.describe())
print(cechy.head())

print(wyniki.head())

