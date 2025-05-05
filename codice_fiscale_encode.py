import csv

def consonants_counter(parola: str):
    consonants = ['b','c','d','f','g','h','l','m','n','p','q','r','s','t','v','z']
    c = 0

    for i in parola.lower():
        if i in consonants:
            c+=1

    return c

def is_consonants(character: str):
    consonants = ['b','c','d','f','g','h','l','m','n','p','q','r','s','t','v','z']

    if character.lower() in consonants:
        return character
    else:
        pass

def is_vowels(character: str):
    vowels = ['a','e','i','o','u']

    if character.lower() in vowels:
        return character
    

def surname_code(cognome: str):
    code = ""

    if len(cognome) < 3:
        for i in cognome.upper():
            code += i
        if len(code) < 3:
            while len(code) < 3:
                code += 'X'
    else:
        if consonants_counter(cognome) < 3:
            for i in cognome.upper():
                if is_consonants(i):
                    code += i
            for i in cognome.upper():
                if is_vowels(i):
                    code += i
                if len(code) == 3:
                    break
        else:
            for i in cognome.upper():
                if is_consonants(i):
                    code += i
                if len(code) == 3:
                    break
            


    return code

def name_code(nome: str):
    code = ""

    if len(nome) < 3:
        for i in nome.upper():
            code += i
        if len(code) < 3:
            while len(code) < 3:
                code += 'X'
    else:
        if consonants_counter(nome) < 3:
            for i in nome.upper():
                if is_consonants(i):
                    code += i
            for i in nome.upper():
                if is_vowels(i):
                    code += i
                if len(code) == 3:
                    break
        elif consonants_counter(nome) > 3:
            tmp = []

            for i in nome.upper():
                if is_consonants(i):
                    tmp.append(i)

            code = f"{tmp[0]}{tmp[2]}{tmp[3]}"
        else:
            while len(code) < 3:
                for i in nome.upper():
                    if is_consonants(i):
                        code += i


    return code


def month_code(mese: str):
    codes = {'01':'A','02':'B','03':'C','04':'D','05':'E','06':'H','07':'L','08':'M','09':'P','10':'R','11':'S','12':'T'}

    if mese in codes.keys():
        return codes[mese]
    
def day_code(giorno: str, sesso: str):
    if sesso.upper() == "F" or sesso.upper() == "FEMMINA":
        return str(int(giorno)+40)
    elif sesso.upper() == "M" or sesso.upper() == "MASCHIO":
        return giorno
    
def load_codici_catastali(file_path):
    codici_catastali = {}
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            comune = row[2].strip()
            codice = row[1].strip()
            codici_catastali[comune] = codice
    return codici_catastali

def municipality_code(comune: str):
    codici_catastali = load_codici_catastali('codici_catastali.csv')
    return codici_catastali.get(comune, "Comune non trovato!")

def control_character(codice_fiscale):
    valori_dispari = {
        '0': 1, '1': 0, '2': 5, '3': 7, '4': 9, '5': 13, '6': 15, '7': 17, '8': 19, '9': 21,
        'A': 1, 'B': 0, 'C': 5, 'D': 7, 'E': 9, 'F': 13, 'G': 15, 'H': 17, 'I': 19, 'J': 21,
        'K': 2, 'L': 4, 'M': 18, 'N': 20, 'O': 11, 'P': 3, 'Q': 6, 'R': 8, 'S': 12, 'T': 14,
        'U': 16, 'V': 10, 'W': 22, 'X': 25, 'Y': 24, 'Z': 23
    }
    
    valori_pari = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
        'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19,
        'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25
    }
    
    conversione_controllo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    somma = 0
    for i, char in enumerate(codice_fiscale[:15]):
        if i % 2 == 0: 
            somma += valori_dispari[char]
        else:
            somma += valori_pari[char]

    resto = somma % 26
    carattere_di_controllo = conversione_controllo[resto]
    
    return carattere_di_controllo



