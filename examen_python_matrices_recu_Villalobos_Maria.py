filas = int(input("Cuantas filas desea? "))
columnas = int(input("Cuantas columnas desea? "))
matriz = []
for i in range(filas):
    fila = []

    for j in range(columnas):
        numero = int(input(f"Ingrese el numero [{i+1},{j+1}]: "))
        fila.append(numero)

    matriz.append(fila)
print("Matriz:")
for i in range(filas):
    print(matriz[i])
suma = 0
for i in range(filas):
    for j in range(columnas):
        suma = suma + matriz[i][j]
print("La sumatoria es:", suma)
producto = 1
for i in range(filas):
    for j in range(columnas):
        producto = producto * matriz[i][j]
print("La productoria es:", producto)
transpuesta = []
for j in range(columnas):
    fila = []

    for i in range(filas):
        fila.append(matriz[i][j])

    transpuesta.append(fila)
print("Matriz transpuesta:")
for i in range(columnas):
    print(transpuesta[i])