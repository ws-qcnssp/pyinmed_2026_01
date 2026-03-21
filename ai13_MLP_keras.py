from sklearn import datasets
from sklearn.model_selection import train_test_split
# from sklearn.neural_network import MLPClassifier
from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.metrics import accuracy_score

dane = datasets.load_breast_cancer()
cechy = dane.data
wyniki = dane.target

# Podział na trening/test
cechy_trening, cechy_test, wyniki_trening, wyniki_test = train_test_split(
    cechy, wyniki, test_size=0.25, random_state=100
)

# model = MLPClassifier(hidden_layer_sizes=(50), random_state=100)
model = Sequential([
    # warstwa wejściowa
    Dense(16, activation='relu', input_shape=(cechy_trening.shape[1])),
    # warstwa ukryta
    Dense(8, activation='relu'),
    # warstwa wyjściowa
    Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(cechy_trening, wyniki_trening, batch_size=10, epochs=50)

wyniki_przewidywane = model.predict(cechy_test)

dokladnosc = accuracy_score(wyniki_test, wyniki_przewidywane)
print(f'Dokładność (accuracy): {dokladnosc}')