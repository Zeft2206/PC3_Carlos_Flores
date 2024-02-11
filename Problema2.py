calificaciones = input('Ingrese las calificaciones separadas con coma: ')

numeros = calificaciones.split(',')
try:
    convertir = [int(i) for i in numeros]
    print(convertir)
except ValueError:
    print("Solo ingresar numeros enteros")
    




