import os

# Directorio donde se almacenan los archivos de los cliente
directorio_clientes = "clientes/"

# Asegurarse de que el directorio existe
if not os.path.exists(directorio_clientes):
    os.makedirs(directorio_clientes)

# Diccionario como tabla hash para asociar el nombre del cliente con su archivo
tabla_clientes = {}

def cargar_clientes():
    """Carga los archivos de cliente existentes en la tabla hash."""
    for archivo_cliente in os.listdir(directorio_clientes):
        if archivo_cliente.endswith(".txt"):
            id_cliente = archivo_cliente.replace("_cliente.txt", "")
            tabla_clientes[id_cliente] = archivo_cliente

def nombre_archivo_cliente(id_cliente):
    """Genera el nombre de archivo para un cliente dado."""
    return os.path.join(directorio_clientes, f"{id_cliente}_cliente.txt")

def crear_cliente():
    """Crea un archivo para un nuevo cliente con la información proporcionada."""
    id_cliente = input("Ingrese el ID del cliente nuevo: ")
    if id_cliente in tabla_clientes:
        print("El cliente ya existe.")
        return

    nombre = input("Ingrese el nombre del cliente nuevo: ")
    contacto = input("Ingrese los detalles de contacto del cliente: ")
    servicio = input("Ingrese el servicio solicitado para el cliente: ")

    archivo_cliente = nombre_archivo_cliente(id_cliente)
    with open(archivo_cliente, 'w') as archivo:
        archivo.write(f"ID: {id_cliente}, Nombre: {nombre}, Contacto: {contacto}\n")
        archivo.write(f"Servicio: {servicio}")
    tabla_clientes[id_cliente] = archivo_cliente
    print(f"Nuevo cliente '{nombre}' creado con el servicio '{servicio}'.")

def leer_cliente():
    """Lee y muestra la información de un cliente existente."""
    id_cliente = input("Ingrese el ID del cliente a leer: ")
    archivo_cliente = tabla_clientes.get(id_cliente)
    if archivo_cliente and os.path.exists(archivo_cliente):
        with open(archivo_cliente, 'r') as archivo:
            print(archivo.read())
    else:
        print("Cliente no encontrado.")

def actualizar_cliente():
    """Actualiza la información de un cliente existente."""
    id_cliente = input("Ingrese el ID del cliente a actualizar: ")
    archivo_cliente = tabla_clientes.get(id_cliente)
    if archivo_cliente and os.path.exists(archivo_cliente):
        nueva_info = input("Ingrese la nueva información del servicio para el cliente: ")
        with open(archivo_cliente, 'a') as archivo:
            archivo.write(f"\nServicio actualizado: {nueva_info}")
        print("Información del cliente actualizada exitosamente.")
    else:
        print("Cliente no encontrado.")

def borrar_cliente():
    """Borra el archivo correspondiente a un cliente."""
    id_cliente = input("Ingrese el ID del cliente a borrar: ")
    archivo_cliente = tabla_clientes.get(id_cliente)
    if archivo_cliente and os.path.exists(archivo_cliente):
        os.remove(archivo_cliente)
        del tabla_clientes[id_cliente]
        print(f"Cliente '{id_cliente}' borrado exitosamente.")
    else:
        print("Cliente no encontrado.")

def mostrar_menu():
    """Muestra el menú de opciones y retorna la opción seleccionada por el usuario."""
    print("\nMenú de Gestión de Clientes")
    print("1. Crear Cliente")
    print("2. Leer Cliente")
    print("3. Actualizar Cliente")
    print("4. Borrar Cliente")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")
    return opcion

def main():
    """Función principal que maneja el flujo del programa."""
    cargar_clientes()  
    while True:
        opcion = mostrar_menu()
        if opcion == '1':
            crear_cliente()
        elif opcion == '2':
            leer_cliente()
        elif opcion == '3':
            actualizar_cliente()
        elif opcion == '4':
            borrar_cliente()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
