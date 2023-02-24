def upper_first_letter(frase:str):
    palabras = frase.split(" ")
    frase = ""
    
    for i in range(len(palabras)):
        letras = list(palabras[i])
        palabras[i] = letras[0].upper()
        
        for a in range(1, len(letras)):
            palabras[i] += letras[a]
        
        frase += palabras[i] + " "
    
    return frase

def upper_with_map(frase:str):
    print(" ".join(frase.replace("  ", " ").title().split(" ")))
    
upper_with_map("esto es una frase de prueba")
print(upper_first_letter("esto es una frase de prueba"))