opcion = int(input("Elije una opción:\n1. Sumar números. \n2. Multiplicar números. \n3. Contar números\n"))
while opcion != 1 and opcion != 2 and opcion != 3:
    opcion = int(input("Opción incorrecta.\n Elije una opción:\n1. Sumar números. \n2. Multiplicar números. \n3. Contar números\n"))

if opcion == 1:
        numeros = int(input("Cuántos números vas a introducir?\n"))
        suma = 0
        total = 0
        numero = 0
        while numeros > suma:
            suma += 1
            numero = int(input("Introduce un número: "))
            total += numero
        print("Suma =", total)
elif opcion == 2:
        numeros = int(input("Cuántos números vas a introducir?\n"))
        suma = 0
        total = 1
        numero = 0
        while numeros > suma:
            suma += 1
            numero = int(input("Introduce un número: "))
            total *= numero
        print("Producto =", total)
else:
        print("Introduce cuantos números quieras, usa 0 para finalizar\n")
        suma = 0
        n = int(input())
        while n != 0:
            n = int(input())
            suma += 1
        print("Has introducido", suma, "números.")
