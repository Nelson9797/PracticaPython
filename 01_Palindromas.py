# Comprueba si una palabra o frase es palindroma

palabra = str(input("Ingresa una palabra: ").lower().replace(" ", ""))
i = len(palabra) - 1
arbalap = palabra[::-1]
    
if palabra == arbalap:
    print("La palabra es palindroma")
else:
    print("La palabra no es palindroma")