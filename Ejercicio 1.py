def OrdenarNombre(nombre_completo):
    """Esta función recibe un "nombre y "apellido y devuelve el "apellido,
    nombre".
    Parámetros:
        -Nombre en el formato "Nombre Apellido"

    Salida:
        -Nombre en el formato "Apellido,Nombre"
        """
    partes = nombre_completo.split()
    nombre = partes[0]
    apellido = partes[1]
    nombre_ordenado = f"{apellido}, {nombre}"
    
    return nombre_ordenado

def ListaNombres(lista_nombres):
    """Esta funcions nos enseña la lista por pantalla y nos
    ordena los nombres
        Parámetros:
        Lista de nombres:esta lista de nombres guarda una cantidad
        indeterminada de nombres este formato:
        ['Nombre Apellido 1','Nombre Apellido 2', ...,'Apellido,Nombre N]

        
        Salida:
        La función retorna la lista de nombres ordenados alfabéticamente en 
        este formato:
        ['Apellido, Nombre 1', 'Apellido, Nombre 2', ...,'Apellido,Nombre N]
        
        """
              
    nombres_ordenados = sorted(lista_nombres, key=OrdenarNombre)
    
    return nombres_ordenados

"""Ejemplo de uso"""
nombres_a_ordenar = ['Juan Pérez', 'Ana López', 'Pedro Gómez', 
                    'María Rodríguez']
nombres_ordenados = ListaNombres(nombres_a_ordenar)

"""Mostrar en pantalla"""
print(nombres_ordenados)