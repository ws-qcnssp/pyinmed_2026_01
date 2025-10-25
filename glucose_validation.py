'''
Skrypt do walidacji stężenia glukozy we krwi
1. wprowadzamy wartość liczbową
2. weryfikujemy, w jakim zakresie została podana wartość
3. weryfikujemy, czy poziom stężenia gl. jest prawidłowy
'''

wprowadzona_liczba = input('Wprowadź stężenie glukozy: ')
wprowadzona_liczba = float(wprowadzona_liczba)
# wprowadzona_liczba = float(input('Wprowadź stężenie glukozy: ')) --> jednolinijkowo

# mg/dl -> 70-100 
# mmol/l -> 3.9 - 5.6
# wartość przyjmijmy jako 40

granica = 40.0

if wprowadzona_liczba < granica:
    jednostka = 'mmol/l'
    dolna_granica = 3.9
    gorna_granica = 5.6
else:
    jednostka = 'mg/dl'
    dolna_granica = 70
    gorna_granica = 100