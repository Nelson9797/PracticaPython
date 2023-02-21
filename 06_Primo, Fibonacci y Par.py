def es_primo(numero):
        for i in range(2, int(numero/2) + 1):
            if numero % i == 0:
                return False
        return True

num = 1
i = 1
fibbo = [1, 1]
primos = [2]

while num != 0:
    num = int(input("Ingresa un numero: "))
    res = str(num)
    es_p = True
    
    while fibbo[-1] < num:
        fibbo.append(fibbo[i - 1] + fibbo[i])
        i += 1

        
    for i in range(primos[-1] + 1, num + 1):
        if i > primos[-1]:
            if es_primo(i):
                primos.append(i)
        
    if num in primos:
        res += " es primo"
    else:
        res += " no es primo"
    
    if num in fibbo:
        res += " es fibbonacci"
    else:
        res += " no es fibonacci"
        
    if num % 2 == 0:
        res += " y es par\n"
    else:
        res += " y es impar\n"
        
    print(res)
    print(fibbo)
    print(primos)