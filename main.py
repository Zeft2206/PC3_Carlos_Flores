import generador_de_numeros

def main():
    # Genera la lista de números aleatorios
    numeros_generados = generador_de_numeros.generar_numeros()

    # Muestra la lista de números generados
    generador_de_numeros.mostrar_lista(numeros_generados)

    # Ordena y muestra la lista de números
    generador_de_numeros.ordenar_lista(numeros_generados)

if __name__ == "__main__":
    main()