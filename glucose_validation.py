'''
Skrypt do walidacji stężenia glukozy we krwi
1. wprowadzamy wartość liczbową
2. weryfikujemy, w jakim zakresie została podana wartość
3. weryfikujemy, czy poziom stężenia gl. jest prawidłowy
'''
granica = 40.0

def wprowadzenie_wartosci():
    wprowadzona_liczba = input('Wprowadź stężenie glukozy: ')
    try:
        wprowadzona_liczba = float(wprowadzona_liczba)
    except ValueError as e:
        print('Podana wartość nie jest liczbą, podaj wartość ułamkową z kropką, nie przecinkiem!')
        return None
    return wprowadzona_liczba
# wprowadzona_liczba = float(input('Wprowadź stężenie glukozy: ')) --> jednolinijkowo

# mg/dl -> 70-100 
# mmol/l -> 3.9 - 5.6
# wartość przyjmijmy jako 40 

def analiza_wyniku(wprowadzona_liczba):
    if wprowadzona_liczba < granica:
        jednostka = 'mmol/l'
        dolna_granica = 3.9
        gorna_granica = 5.6
    else:
        jednostka = 'mg/dl'
        dolna_granica = 70
        gorna_granica = 100

    if dolna_granica <= wprowadzona_liczba <= gorna_granica:
        # print(f'{wprowadzona_liczba} {jednostka} -> w normie!')
        # print('{licz} {jedn} -> w normie!'.format(licz=wprowadzona_liczba, jedn=jednostka))
        # print(wprowadzona_liczba, jednostka, '-> w normie!')
        poziom = 'w normie!'
    elif wprowadzona_liczba < dolna_granica:
        # print(f'{wprowadzona_liczba} {jednostka} -> poniżej normy!')
        poziom = 'poniżej normy!'
    else:
        # print(f'{wprowadzona_liczba} {jednostka} -> powyżej normy!')
        poziom = 'powyżej normy!'
    return jednostka, poziom


liczba = wprowadzenie_wartosci()
if liczba is None:
    print('Koniec skryptu.')
    exit()
jedn, poz = analiza_wyniku(liczba)
print(f'{liczba} {jedn} - {poz}')
