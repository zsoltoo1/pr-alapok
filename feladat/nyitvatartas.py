aktualis_ora = int(input("Hány óra van most? "))

if 8 <= aktualis_ora < 16:
    print("A bolt nyitva van. Ennyi órád van még odaérni:", 16 - aktualis_ora)
else:
    print("A bolt zárva van. Holnap próbálkozz meg!")