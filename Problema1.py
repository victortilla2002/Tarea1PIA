def procesar_lista_enteros(lista):
    nueva_lista = []

    # 1. Eliminar los números negativos
    for numero in lista:
        if numero >= 0:
            # 2. Evitar repetir números
            if numero not in nueva_lista:
                nueva_lista.append(numero)

    # 3. Ordenar la lista de menor a mayor
    nueva_lista.sort()

    return nueva_lista


# Ejemplo de uso
numeros = [4, -1, 2, 4, 3, -5, 2]
resultado = procesar_lista_enteros(numeros)
print(resultado)  # Salida esperada: [2, 3, 4]
