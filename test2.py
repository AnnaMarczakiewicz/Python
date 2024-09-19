import random
dystans = random.randint(1,100000)
cena_paliwa = float(input("Podaj aktualną cenę paliwa za litr"))
spalanie = float(input("Podaj średnie spalanie paliwa (litry na 100 km): "))

# Obliczenie zużycia paliwa
zuzycie_paliwa = (spalanie / 100) * dystans

# Obliczenie kosztu podróży
koszt_podrozy = zuzycie_paliwa * cena_paliwa

# Wyświetlenie wyników
print("Przewidywane zużycie paliwa w litrach:", zuzycie_paliwa)
print("Szacowany koszt podróży w zł:", koszt_podrozy)

