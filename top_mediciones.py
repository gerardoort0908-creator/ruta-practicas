
def resumen(mediciones):
    """Devuele resumen con los 3 primeros y ultimos y la mediana y el promedio"""
    n = len(mediciones)
    total = sum(mediciones)
    promedio = total / n
    ordenados = sorted(mediciones)
    if n % 2 == 0:
        mediana = (ordenados[n//2 - 1] + ordenados[n//2]) / 2
    else:
        mediana = ordenados[n//2]
        
        
    return {
        "Promedio": promedio,
        "Ultimos_3": ordenados[-3:], 
        "Primeros_3" : ordenados[:3], 
        "Mediana": mediana
        }

   
    
mediciones_1 = [12.45, 12.38, 12.51, 12.42, 12.47]

mediciones_2 = [15.2, 16.4, 14.8, 15.9, 17.1, 16.2]

mediciones_3 = [20, 25, 30, 35, 40]

mediciones = [12.45, 12.38, 12.51, 12.42, 12.47, 12.39, 12.55, 12.41, 12.49, 12.36, 12.53, 12.44, 12.48, 12.40, 12.52]

resultado = resumen(mediciones)
for clave, valor in resultado.items():
    print(f"{clave}: {valor}")
    
    
    