import random

bucle = True
puntuacion = [0, 0]

while bucle:

    print("\n1.-Piedra 2.-Papel 3.-Tijeras")
    elec_usuario = int(input("Escribe tu elección: "))
    elec_maquina = random.randint(1,3)
    
    if elec_usuario == 1:
        print("\nElegiste piedra")
        if elec_maquina == 1:
            print("La maquina tambien eligio piedra, Empate¡\n")
            
        if elec_maquina == 2:
            print("La maquina eligio papel, Perdiste¡\n")
            puntuacion[1] += 1
            
        if elec_maquina == 3:
            print("La maquina eligio tijeras, Ganaste¡\n")
            puntuacion[0] += 1
            
    elif elec_usuario == 2:
        print("\nElegiste papel")
        if elec_maquina == 1:
            print("La maquina tambien eligio piedra, Ganaste¡\n")
            puntuacion[0] += 1
            
        if elec_maquina == 2:
            print("La maquina eligio papel, Empate¡\n")
            
        if elec_maquina == 3:
            print("La maquina eligio tijeras, Perdiste¡\n")
            puntuacion[1] += 1
            
    elif elec_usuario == 3:
        print("\nElegiste tijeras")
        if elec_maquina == 1:
            print("La maquina tambien eligio piedra, Perdiste¡\n")
            puntuacion[1] += 1
            
        if elec_maquina == 2:
            print("La maquina eligio papel, Ganaste¡\n")
            puntuacion[0] += 1
            
        if elec_maquina == 3:
            print("La maquina eligio tijeras, Empate¡\n")
            
    else:
        print("\n!ESA NO ES UNA OPCIÓN¡\n")
    
    print(f"Puntuación: {puntuacion}")
    bucle = "s" == input("¿Quieres volver a jugar? (s/n): ")
    
print(f"\nPuntuacion final: {puntuacion}")

