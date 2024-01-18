def main():
    helyes_felhasznalonev = "bori99"
    helyes_jelszo = "Szivecske<3"

    print("Adja meg a felhasználónevét!", end=" ")
    felhasznalonev = input().strip()

    print("Adja meg a jelszavát!", end=" ")
    jelszo = input().strip()

    while felhasznalonev != helyes_felhasznalonev or jelszo != helyes_jelszo:
        print("Hibás felhasználónév vagy jelszó. Próbálja újra.")
        
        print("Adja meg a felhasználónevét!", end=" ")
        felhasznalonev = input().strip()

        print("Adja meg a jelszavát!", end=" ")
        jelszo = input().strip()

    print("Belépés engedélyezve.")

if __name__ == "__main__":
    main()