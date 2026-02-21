from sklearn.datasets import fetch_openml

dane = fetch_openml(data_id=1506, as_frame=True, parser='auto')
cechy = dane.data
wyniki = dane.target

print(cechy.head())
print(cechy.info())

cechy_num = cechy.select_dtypes(include=['int64', ''])
