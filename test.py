dystans = float(input("Podaj drogę pokonaną przez samochód (w km): "))
spalanie = float(input("Podaj średnie spalanie paliwa (litry na 100 km): "))

# Stała cena paliwa
cena_paliwa = 6.5  # zł za litr

# Obliczenie zużycia paliwa
zuzycie_paliwa = (spalanie / 100) * dystans

# Obliczenie kosztu podróży
koszt_podrozy = zuzycie_paliwa * cena_paliwa

# Wyświetlenie wyników
print("Przewidywane zużycie paliwa w litrach:", zuzycie_paliwa)
print("Szacowany koszt podróży w zł:", koszt_podrozy)
# test