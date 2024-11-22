def load_file(file_path):
    """
    Leser en tekstfil og returnerer innholdet som en liste med linjer.
    Hvis filen ikke finnes, returneres None og en feilmelding vises.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()  # Leser innholdet som en liste med linjer
    except FileNotFoundError:
        print(f"Feil: Filen '{file_path}' ble ikke funnet.")  # Feilmelding
        main_menu()

def search_word(content, search_term):
    """
    Søker etter et ord eller en tekst i en liste med linjer (content).
    Returnerer en liste med treff som inneholder linjenummer og linjeinnhold.
    """
    results = []
    for line_number, line in enumerate(content, start=1):  
        if search_term.lower() in line.lower():  # Søker case-insensitivt
            results.append((line_number, line.strip()))  # Legger til linjetreff
    return results

def list_files():
    """
    Returnerer en liste med tilgjengelige filer som brukeren kan velge fra.
    """
    return [
        "DetteErGøy.txt",
        "leandro.txt",
        "tekstfil1.txt",
        "tekstfil2.txt",
        "tekstfil3.txt"
    ]

def choose_file():
    """
    Lar brukeren velge en fil fra listen med tilgjengelige filer.
    Returnerer navnet på den valgte filen.
    """
    files = list_files()  # Henter listen med filer
    print("\nTilgjengelige filer:")
    for idx, file_name in enumerate(files, start=1):  # Viser filer med nummer
        print(f"{idx}. {file_name}")
    
    while True:  # Løkke for gyldig input
        try:
            choice = int(input("Velg nummeret på filen du vil bruke: "))
            if 1 <= choice <= len(files):  # Sjekker om valget er innenfor rekkevidde
                return files[choice - 1]  # Returnerer valgt fil
            else:
                print("Ugyldig valg. Skriv inn et tall fra listen.")
        except ValueError:
            print("Ugyldig input. Skriv inn et tall.")

def show_file_content(file_path):
    """
    Leser og viser innholdet i en valgt fil.
    """
    content = load_file(file_path)  # Leser innholdet i filen
    if content:
        print(f"\nInnhold i {file_path}:\n{'-' * 40}")
        print("".join(content))  # Skriver ut innholdet linje for linje
    else:
        print("Ingen innhold å vise.")  # Feilmelding hvis filen ikke kan leses

def search_in_file(file_path):
    """
    Lar brukeren søke etter tekst i en valgt fil.
    Viser treffene for hver linje som inneholder søketeksten.
    """
    content = load_file(file_path)  # Leser innholdet i filen
    if content:
        while True:  # Tillater flere søk i samme fil
            search_term = input("\nSkriv inn teksten du vil søke etter ('return' eller 'exit' for å gå tilbake): ")
            if search_term.lower() in ["return", "exit"]:  
                # går tilbake til hovedmenyen hvis brukeren skriver "return" eller "exit"
                break
            results = search_word(content, search_term)  # Søker i filen
            if results:
                print(f"\nTreff for '{search_term}' i {file_path}:")
                for line_number, line in results:
                    print(f"Linje {line_number}: {line}")  # Viser trefflinjer
            else:
                print(f"Ingen treff for '{search_term}' i {file_path}.")
    else:
        print("Kunne ikke åpne filen.")  # Feilmelding hvis filen ikke kan leses

def main_menu():
    """
    Viser hovedmenyen og håndterer brukerens valg.
    Lar brukeren velge mellom å vise filinnhold, søke i en fil eller avslutte programmet.
    """
    while True:
        print("\nHva vil du gjøre?")
        print("1. Vis innholdet i en fil")
        print("2. Søk etter tekst i en fil")
        print("3. Avslutt")
        
        choice = input("Velg et alternativ (1-3): ")  # Brukerens menyvalg
        
        if choice == "1":  # Brukeren vil vise innholdet i en fil
            file_path = choose_file()  # Lar brukeren velge fil
            show_file_content(file_path)  # Viser innholdet i den valgte filen
        elif choice == "2":  # Brukeren vil søke i en fil
            file_path = choose_file()  # Lar brukeren velge fil
            search_in_file(file_path)  # Søker i innholdet i den valgte filen
        elif choice == "3": 
            while True:  # løkke for å sikre korrekt input
                bekreftelse = input("Er du sikker på at du vil avslutte? J/N ").strip().lower()  
                # Fjern mellomrom og mulig å bruke små bokstaver uten å repetere kode
                if bekreftelse == "j":
                    print("Avslutter programmet. Ha en fin dag!")
                    exit()
                elif bekreftelse == "n":
                    main_menu()
                    break  # Avslutt løkken når brukeren ikke vil avslutte
                else:
                    print("Feil, skriv enten J eller N.")  

        else:
            print("Ugyldig valg. Skriv inn 1, 2 eller 3.")  # Feilmelding for ugyldige valg

if __name__ == "__main__":
    main_menu()  # Starter hovedprogrammet
