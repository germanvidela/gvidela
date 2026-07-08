def mostrar_menu():
    print("\n" + "="*40)
    print("      MENÚ PRINCIPAL - VIDEOJUEGOS")
    print("="*40)
    print("1. Agregar nuevo juego")
    print("2. Ver catálogo de juegos")
    print("3. Buscar juego por plataforma")
    print("4. Actualizar stock")
    print("5. Salir")
    print("="*40)

def agregar_juego():
    print("\n--- Agregar Nuevo Juego ---")
    nombre = input("Nombre del juego: ")
    
    # Validación de plataforma
    print("Plataforma (PC, PS5, Xbox): ")
    plataforma = input("> ").strip().capitalize()
    while plataforma not in ["Pc", "Ps5", "Xbox"]:
        print("Plataforma no válida. Intenta de nuevo (PC, PS5, Xbox): ")
        plataforma = input("> ").strip().capitalize()

    tipo = input("Tipo de juego (ej. Acción, RPG, Deportes): ")
    version = input("Versión (ej. Estándar, Deluxe, GOTY): ")
    
    # Validación de Precio y Stock
    try:
        precio = float(input("Precio ($): "))
        stock = int(input("Stock disponible: "))
    except ValueError:
        print("Error: El precio y el stock deben ser números. Intenta de nuevo.")
        return

    nuevo_juego = {
        "nombre": nombre,
        "plataforma": plataforma,
        "tipo": tipo,
        "version": version,
        "precio": precio,
        "stock": stock
    }
    
    inventario.append(nuevo_juego)
    print(f"¡Juego '{nombre}' agregado exitosamente!")

def ver_catalogo():
    if not inventario:
        print("\nEl catálogo está vacío.")
        return
        
    print("\n--- Catálogo de Juegos ---")
    for i, juego in enumerate(inventario, start=1):
        print(f"\nJuego {i}: {juego['nombre']}")
        print(f"  Plataforma: {juego['plataforma']} | Versión: {juego['version']}")
        print(f"  Tipo: {juego['tipo']}")
        print(f"  Precio: ${juego['precio']:.2f} | Stock: {juego['stock']}")

def buscar_por_plataforma():
    print("\n--- Buscar por Plataforma ---")
    plat_buscar = input("Ingresa plataforma (PC, PS5, Xbox): ").strip().capitalize()
    
    encontrados = [j for j in inventario if j['plataforma'] == plat_buscar]
    
    if not encontrados:
        print(f"No hay juegos registrados para {plat_buscar}.")
    else:
        print(f"\nJuegos para {plat_buscar}:")
        for juego in encontrados:
            print(f"- {juego['nombre']} | {juego['version']} | Precio: ${juego['precio']:.2f} | Stock: {juego['stock']}")

def actualizar_stock():
    if not inventario:
        print("\nNo hay juegos en el inventario para actualizar stock.")
        return
        
    print("\n--- Actualizar Stock ---")
    nombre_juego = input("Nombre del juego a actualizar: ")
    
    for juego in inventario:
        if juego['nombre'].lower() == nombre_juego.lower():
            try:
                nuevo_stock = int(input(f"Nuevo stock para '{juego['nombre']}': "))
                juego['stock'] = nuevo_stock
                print("Stock actualizado exitosamente.")
                return
            except ValueError:
                print("Error: Ingresa un número válido.")
                return
                
    print("Juego no encontrado en el inventario.")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-5): ")
    
    if opcion == '1':
        agregar_juego()
    elif opcion == '2':
        ver_catalogo()
    elif opcion == '3':
        buscar_por_plataforma()
    elif opcion == '4':
        actualizar_stock()
    elif opcion == '5':
        print("\n¡Gracias por usar el sistema de gestión de juegos! Saliendo...")
        break
    else:
        print("\nOpción no válida. Por favor, elige un número del 1 al 5.")