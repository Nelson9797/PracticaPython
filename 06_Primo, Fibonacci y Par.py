num = int(input("Ingresa un numero: "))
fibbo = [1, 1]
primo = []
res = str(num) + " "

def es_par():
    if num % 2 == 0:
        return True
    else:
        return False
    
def es_fibbonacci():
    i = 0
    while fibbo[-1] < num:
        fibbo.append(fibbo[i] + fibbo[i+1])
        i += 1
    
    if num in fibbo:
        return True
    else:
        return False

def es_primo():
    
    for i in range(1, num + 1):
        if i % num == 0:
            return False
        else:
            return True

if es_primo():
    res += "es primo, "
else:
    res += "no es primo, "
     
if es_fibbonacci():
    res += "fibbonacci "
else:
    res += "no es fibonacci "
    
if es_par():
    res += "y es par"
else:
    res += "y es impar"
    
print(res)