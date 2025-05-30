import random
import math

#hago la importacion de librerias math y randon para agilizar este problema de t2
random.seed(42)
#todos los numero a volver a ejecutar el codigo seran alatorios , entonces seran cordenadas diferentes 
#aqui genero mis funciones profesor
def generar_coordenadas(n):
    coordenadas = []
    for i in range(n):
        x = random.randint(-81, 81)
        y = random.randint(-81, 81)
        coordenadas.append([x, y])
    return coordenadas

def calcular_distancia(coordenada):
    x, y = coordenada
    return math.sqrt(x**2 + y**2)

def es_valida(coordenada):
    x, y = coordenada
    return x > 0 and y < 0

def dividir_y_conquistar(coordenadas):
    if not coordenadas:
        return None
    
    if len(coordenadas) == 1:
        if es_valida(coordenadas[0]):
            return coordenadas[0]
        else:
            return None
    
    if len(coordenadas) == 2:
        coord1, coord2 = coordenadas[0], coordenadas[1]
        valida1, valida2 = es_valida(coord1), es_valida(coord2)
        
        if valida1 and valida2:
            if calcular_distancia(coord1) >= calcular_distancia(coord2):
                return coord1
            else:
                return coord2
        elif valida1:
            return coord1
        elif valida2:
            return coord2
        else:
            return None
    
    # dividir
    mitad = len(coordenadas) // 2
    izquierda = coordenadas[:mitad]
    derecha = coordenadas[mitad:]
    
    # conquistar
    max_izquierda = dividir_y_conquistar(izquierda)
    max_derecha = dividir_y_conquistar(derecha)
    
    # combinar
    if max_izquierda is None and max_derecha is None:
        return None
    elif max_izquierda is None:
        return max_derecha
    elif max_derecha is None:
        return max_izquierda
    else:
        if calcular_distancia(max_izquierda) >= calcular_distancia(max_derecha):
            return max_izquierda
        else:
            return max_derecha

# ejemplo
print("=== EJEMPLO DE EJECUCIÓN ===")
print("Cantidad de coordenadas: 10")

coordenadas = generar_coordenadas(10)

print("\nCoordenadas generadas:")
for i, coord in enumerate(coordenadas):
    x, y = coord
    distancia = calcular_distancia(coord)
    valida = "✓" if es_valida(coord) else "✗"
    print(f"[{x:3d}, {y:3d}] - Distancia: {distancia:6.2f} - Válida: {valida}")

# aqui esta divede y vencerás
coordenadas_validas = [coord for coord in coordenadas if es_valida(coord)]
print(f"\nCoordenadas válidas (X>0, Y<0): {len(coordenadas_validas)}")

resultado = dividir_y_conquistar(coordenadas)

print("\nRESULTADO:")
if resultado:
    x, y = resultado
    distancia = calcular_distancia(resultado)
    print(f"Coordenada más alejada: [{x}, {y}]")
    print(f"Distancia: {distancia:.4f}")
else:
    print("Sin coordenadas válidas")

#usasmos el dividde y conquista para hacer el problema en partes mas pequeñas donde cada 
#iteracion  se divide 