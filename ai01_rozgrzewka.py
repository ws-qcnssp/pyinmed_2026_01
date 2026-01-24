# 1. Zaimportuj bibliotekę Pandas jako pd
import pandas as pd

# 2. Utwórz słownik danych z trzema kluczami: 'Imię', 'Wiek', 'Miasto' i odpowiednimi listami wartości - po 5 elementów każda
slownik = {
    'Imię': ['Kuba', 'Adam', 'Ewa', 'Paweł', 'Natalia'], 
    'Wiek': [23, 45, 53, 28, 13],
    'Miasto': ['Kraków', 'Warszawa', 'Poznań', 'Wrocław', 'Kraków']
}
print(slownik)

# 3. Utwórz DataFrame z powyższego słownika
df = pd.DataFrame(slownik)
print(df)

# 4. Wyświetl informacje o DataFrame za pomocą metody "info", "describe" oraz pierwsze 3 wiersze za pomocą metody "head"
print('Metoda info:')
print(df.info())
print('Metoda describe:')
print(df.describe())
print('Metoda head:')
print(df.head())

# 5. Dodaj nową kolumnę 'Kraj' z wartością 'Polska' dla wszystkich wierszy
df['Kraj'] = 'Polska'

# 6. Filtruj DataFrame, aby wyświetlić tylko osoby starsze niż 30 lat


# 7. Zapisz DataFrame do pliku CSV o nazwie 'dane_osobowe.csv' bez indeksów

