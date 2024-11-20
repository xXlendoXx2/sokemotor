def printMeny():
    print("------------------- Søkemotor Meny -------------------")
    print("| 1. Vis innholdet i en fil                          |")
    print("| 2. Søk etter tekst i en fil                        |")
    print("| 3. Avslutt                                         |")
    print("------------------------------------------------------")
    menyvalg = input("Velg et alternativ (1-3): ")
    utfoerMenyvalg(menyvalg)

def utfoerMenyvalg(valgtTall):
    if valgtTall == "1":
        visInnhold()
    elif valgtTall == "2":
        sokIFil()
    elif valgtTall == "3":
        print("Avslutter programmet.")
        exit()
    else:
        print("Ugyldig valg. Prøv igjen.")
        printMeny()

def listFiler():
    # Faste filer i programmet
    return [
        "DetteErGøy.txt",
        "leandro.txt",
        "tekstfil1.txt",
        "tekstfil2.txt",
        "tekstfil3.txt",
    ]

def visInnhold():
    filer = listFiler()
    for idx, fil in enumerate(filer, 1):
        print(f"{idx}. {fil}")
    try:
        valg = int(input("Velg nummeret til filen du vil vise: "))
        valgtFil = filer[valg - 1]
        with open(valgtFil, "r", encoding="utf-8") as file:
            print(f"\nInnholdet i {valgtFil}:\n{'-' * 50}")
            print(file.read())
    except (IndexError, ValueError, FileNotFoundError):
        print("Feil! Sjekk filnummeret eller filen eksisterer kanskje ikke.")
    printMeny()

def sokIFil():
    filer = listFiler()
    for idx, fil in enumerate(filer, 1):
        print(f"{idx}. {fil}")
    try:
        valg = int(input("Velg nummeret til filen du vil søke i: "))
        valgtFil = filer[valg - 1]
        soketxt = input("Skriv inn teksten du vil søke etter: ")
        with open(valgtFil, "r", encoding="utf-8") as file:
            treff = [linje.strip() for linje in file if soketxt.lower() in linje.lower()]
            if treff:
                print(f"\nTreff for '{soketxt}' i {valgtFil}:\n{'-' * 50}")
                for linje in treff:
                    print(linje)
            else:
                print(f"Ingen treff for '{soketxt}' i {valgtFil}.")
    except (IndexError, ValueError, FileNotFoundError):
        print("Feil! Sjekk filnummeret eller filen eksisterer kanskje ikke.")
    printMeny()

# Start menyen
printMeny()
