from encordadora import Encordadora

def menu():
    mi_encordadora = Encordadora()
    
    while True:
        print("\nOpciones:")
        print("1. Ajustar patrón de encordado")
        print("2. Tensar cuerda")
        print("3. Cortar cuerda")
        print("4. Mostrar estado de la encordadora")
        print("5. Mostrar suma de tensiones")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                cuerdas_verticales = int(input("Ingrese cantidad de cuerdas verticales: "))
                cuerdas_horizontales = int(input("Ingrese cantidad de cuerdas horizontales: "))
                mi_encordadora.ajustar_patron_encordado(cuerdas_verticales, cuerdas_horizontales)
                print(f"Patrón ajustado a {cuerdas_verticales} cuerdas verticales y {cuerdas_horizontales} cuerdas horizontales.")
            except ValueError as e:
                print(f"Error: {e}")
        
        elif opcion == '2':
            try:
                tipo_tension = input("Ingrese el tipo de tensión (tensión uniforme/tensión diferenciada): ")
                tension_vertical = float(input("Ingrese la tensión vertical: "))
                tension_horizontal = float(input("Ingrese la tensión horizontal: "))
                mi_encordadora.tensar_cuerda(tipo_tension, tension_vertical, tension_horizontal)
                print("Cuerda tensada con éxito.")
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '3':
            try:
                mensaje = mi_encordadora.cortar_cuerda()
                print(mensaje)
            except ValueError as e:
                print(f"Error: {e}")

        elif opcion == '4':
            print(mi_encordadora)  # Usa el método __str__

        elif opcion == '5':
            print(f"Suma de tensiones: {len(mi_encordadora)} kg")  # Usa el método __len__

        elif opcion == '6':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
