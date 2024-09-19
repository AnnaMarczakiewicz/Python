import math

# Pobranie długości boków trójkąta
a = float(input("Podaj długość boku a: "))
b = float(input("Podaj długość boku b: "))
c = float(input("Podaj długość boku c: "))

# Obliczenie półobwodu
p = (a + b + c) / 2

# Obliczenie pola za pomocą wzoru Herona
pole = math.sqrt(p * (p - a) * (p - b) * (p - c))

# Wyświetlenie wyniku
print(f"Pole trójkąta wynosi: {pole} jednostek kwadratowych")