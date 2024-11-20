def load_file(file_path):
    """leser tekstfil fra en filbane (file_path) 
    returnerer innholdet i filen som en liste med linjer og den 
    den printer ut at det er en feil hvis den ikke finner filen du har søkt etter."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Feil: Finner ikke filen {file_path}.")
        main()

def search_word(content, search_term):
    """Søker etter et ord i teksten og returnerer linjer som inneholder ordet."""
    results = []
    for line_number, line in enumerate(content, start=1):
        if search_term.lower() in line.lower():  # Case-insensitivt søk
            results.append((line_number, line.strip()))
    return results

def print_results(results, search_term):
    """Skriver ut resultatene av søket til terminalen."""
    if results:
        print(f"Fant '{search_term}' i følgende linjer:")
        for line_number, line in results:
            print(f"Linje {line_number}: {line}")
    else:
        print(f"Fant ingen resultater for '{search_term}'.")

def main():
    """Hovedfunksjon for søkemotoren."""
    print("Velkommen til den Leandro sin søkemotor!")
    file_path = input("Skriv inn filnavnet : ")
    content = load_file(file_path)
    
    if not content:  # Avbryt hvis filen ikke finnes
        return
    
    while True:
        search_term = input("Skriv inn ordet du vil søke etter (trykk enter for å se alt, 'exit' eller 'avslutt' for å avslutte): ")
        if search_term.lower() in ['avslutt','exit']:
            print("Avslutter søkemotoren. Ha en fin dag!")
            break
        results = search_word(content, search_term)
        print_results(results, search_term)

if __name__ == "__main__":
    main()
