print('''Jaką operację chcesz wykonać?
      1) dodawanie
      2) odejmowanie
      3) mnożenie
      4) dzielenie
      5) potęgowanie''')

wybor = int(input('Wpisz numer operacji: '))
if not(0 < wybor < 6):
    print('Niepoprawny numer operacji')
    exit()

zmienna1 = float(input('Podaj argument 1: '))
zmienna2 = float(input('Podaj argument 2: '))

if wybor == 1:
    wynik = zmienna1 + zmienna2
elif wybor == 2:
    wynik = zmienna1 - zmienna2
elif wybor == 3:
    wynik = zmienna1 * zmienna2
elif wybor == 4:
    if zmienna2 == 0:
        print('Nie można dzielić przez zero!!!')
        exit()
    wynik = zmienna1 / zmienna2
elif wybor == 5:
    wynik = zmienna1 ** zmienna2
print(f'Wynik: {round(wynik,2)}')
