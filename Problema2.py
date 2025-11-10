def frecuencia_palabras(lista_palabras):
    ruta_archivo = "Texto.txt"  # Texto a leer 

    # Crear un diccionario con las palabras y poner su contador a 0
    frecuencias = {}
    for palabra in lista_palabras:
        frecuencias[palabra.lower()] = 0

    try:
        # Abrir el archivo de texto
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            texto = archivo.read()

            # Pasar todo a minúsculas
            texto = texto.lower()

            # Quitar signos de puntuación comunes
            for signo in [".", ",", "!", "?", ":", ";", "(", ")", "\""]:
                texto = texto.replace(signo, "")

            # Separar el texto en palabras
            palabras = texto.split()

            # Contar cuántas veces aparece cada palabra de la lista
            for palabra in palabras:
                if palabra in frecuencias:
                    frecuencias[palabra] += 1

        # Ordenar las palabras alfabéticamente
        frecuencias_ordenadas = dict(sorted(frecuencias.items()))

        return frecuencias_ordenadas

    except FileNotFoundError:
        print("Error: No se encontró el archivo 'Texto.txt'.")
        return None


# Programa principal
if __name__ == "__main__":
    print("=== FRECUENCIA DE PALABRAS EN TEXTO.TXT ===\n")
    
    # El usuario escribe las palabras separadas por espacios
    lista =["programa","espacio" ,"facil"]

    resultado = frecuencia_palabras(lista)

    if resultado:
        print("\nFrecuencia de palabras:\n")
        for palabra, veces in resultado.items():
            print(f"{palabra}: {veces}")
