from sklearn import datasets
from sklearn.model_selection import train_test_split
# from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

dane = datasets.load_breast_cancer()
cechy = dane.data
wyniki = dane.target