n = int(input("¿Cuantas mediciones quieres?"))
total = 0
mediciones = []

for i in range(n):
    
    medicion = float(input("Medicion: "))
    mediciones.append(medicion)
    
    total = medicion + total
    if i == 0:
        minimo = medicion
        maximo = medicion 
    elif minimo > medicion:
        minimo = medicion
    elif maximo < medicion:
        maximo = medicion
        
promedio = total / n

print(f"Total: {total:.2f}")
print(f"Promedio: {promedio:.2f}")
print(f"Minimo: {minimo:.2f}")
print(f"Maximo: {maximo:.2f}")
print(mediciones)
        