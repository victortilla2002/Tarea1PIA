def operar_conjuntos(lista1, lista2):
    # Convertir las listas en conjuntos (así se eliminan los duplicados)
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)

    # Crear un diccionario con los resultados
    resultados = {
        "interseccion": conjunto1 & conjunto2,        # Elementos comunes
        "union": conjunto1 | conjunto2,                # Todos sin duplicados
        "diferencia_simetrica": conjunto1 ^ conjunto2  # En uno u otro, pero no en ambos
    }

    return resultados


# Programa principal
if __name__ == "__main__":
    print("=== TRABAJO CON CONJUNTOS ===\n")

    # Pedimos al usuario dos listas de números enteros
    lista1 = input("Escribe los números de la primera lista separados por espacios: ").split()
    lista2 = input("Escribe los números de la segunda lista separados por espacios: ").split()

    # Convertimos las entradas a enteros
    lista1 = [int(num) for num in lista1]
    lista2 = [int(num) for num in lista2]

    # Llamamos a la función
    resultado = operar_conjuntos(lista1, lista2)

    # Mostramos los resultados
    print("\nResultados:")
    print(f"Intersección: {resultado['interseccion']}")
    print(f"Unión: {resultado['union']}")
    print(f"Diferencia simétrica: {resultado['diferencia_simetrica']}")
