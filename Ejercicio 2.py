alumnado = {}

def añadir_alumno():
    """Esta función añade el alumno y lo almacena,
     Parámetros
        -nombre, aprobado, alumno,
     Salida
     -Print(...)

        """
    nombre = input("Ingrese el nombre del alumno/a: ")
    aprobado = input("¿Aprobado? (Sí/No): ").lower() == "sí"
    alumnado[nombre] = aprobado
    print(f"¡Alumno/a {nombre} añadido/a correctamente!")

def numero_aprobados():
    """Muestra el numero de aprobados y los almacena en una variable
        Parámetros
        -número de aprobados:
        Salida
        -
            """
    num_aprobados = sum(aprobado for aprobado in alumnado.values())
    print(f"El número de aprobados es: {num_aprobados}")

def mostrar_alumnado():
    """Muestra el alumno en una lista y nos dice si esta aprobado o 
    suspendido
    Parámetros:
    -Lista de alumnos/a
    Salida:
    -print(nombre,resultado)
        """
    print("Listado de Alumnos/as:")
    for nombre, aprobado in alumnado.items():
        resultado = "Aprobado" if aprobado else "Suspendido"
        print(f"{nombre}: {resultado}")

def ejecutar_programa():
    """Finalmente esta función ejecutaria nuestro programa añadiendo un menú
        despegable
        Parámetros:
        -Añadir alumno,Numero de aprobados,mostrar todo el alumnado.
        Salida:
        -Opción 1 , Opción 2 y Opción 3
        """
    while True:
        print("\nMenú:")
        print("(1) Añadir alumno/a")
        print("(2) Número de aprobados")
        print("(3) Mostrar todo el alumnado")

        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == "1":
            añadir_alumno()
        elif opcion == "2":
            numero_aprobados()
        elif opcion == "3":
            mostrar_alumnado()
        else:
            print("Opción no válida. Inténtelo de nuevo.")

if __name__ == "__main__":
    ejecutar_programa()

