class Lote:
    def __init__(self, numero, disponible):
        self.numero = numero
        self.disponible = disponible

class LoteosDuoc:
    def __init__(self):
        self.lotes = []

    def ver_disponibilidad_lotes(self):
        print("Lotes disponibles:")
        for i in range(3): 
            for j in range(3):
                lote = self.lotes[i * 3 + j]
                if lote.disponible:
                    print("[ ]", end=" ") 
                else:
                    print("[X]", end=" ")  
            print() 

    def seleccionar_lote(self):
        numero_lote = int(input("Ingrese el número de lote que desea seleccionar: "))
        lote = self.lotes[numero_lote - 1]
        if lote.disponible:
            lote.disponible = False
            print(f"El lote {lote.numero} ha sido seleccionado.")
        else:
            print("El lote seleccionado no está disponible.")

    def ver_detalles_lote(self):
        numero_lote = int(input("Ingrese el número de lote para ver sus detalles: "))
        lote = self.lotes[numero_lote - 1]
        print(f"Detalles del lote {lote.numero}:")
        print(f"Disponible: {'Sí' if lote.disponible else 'No'}")

    def ver_clientes(self):
       
        print("Mostrar clientes")

    def ejecutar(self):
        while True:
            print("\n==== Menú ====")
            print("1. Ver disponibilidad de lotes")
            print("2. Seleccionar un lote")
            print("3. Ver detalles del lote seleccionado")
            print("4. Ver clientes")
            print("5. Salir")

            opcion = input("Ingrese el número de la opción que desea ejecutar: ")

            if opcion == "1":
                self.ver_disponibilidad_lotes()
            elif opcion == "2":
                self.seleccionar_lote()
            elif opcion == "3":
                self.ver_detalles_lote()
            elif opcion == "4":
                self.ver_clientes()
            elif opcion == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción inválida. Por favor, ingrese un número válido.")


if __name__ == "__main__":
    loteos_duoc = LoteosDuoc()
    
    loteos_duoc.lotes = [
        Lote("1", True),
        Lote("2", True),
        Lote("3", True),
        Lote("4", True),
        Lote("5", True),
        Lote("6", True),
        Lote("7", True),
        Lote("8", True),
        Lote("9", True),
    ]
    loteos_duoc.ejecutar()
