"""
Examen: Gestión de Inventario con Persistencia JSON y Programación Orientada a Objetos
Autor/a: Carlos Norte
Fecha: 4 de Noviembre del 2025

Objetivo:
Desarrollar una aplicación orientada a objetos que gestione un inventario de productos
con persistencia de datos en ficheros JSON y uso de listas y diccionarios anidados.

Clases requeridas:
- Proveedor
- Producto
- Inventario

"""

import json
import os


# ======================================================
# Clase Proveedor
# ======================================================

class Proveedor:
    def __init__(self, codigo, nombre, contacto):
        self.codigo = codigo
        self.nombre = nombre
        self.contacto = contacto


    def __str__(self):
        # TODO: devolver una cadena legible con el nombre y el contacto del proveedor
        return f"{self.codigo}, {self.nombre}, {self.contacto}"


# ======================================================
# Clase Producto
# ======================================================

class Producto:
    def __init__(self, codigo, nombre, precio, stock, proveedor):
        # TODO: definir los atributos de la clase
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor = proveedor


    def __str__(self):
        # TODO: devolver una representación legible del producto
        # Ejemplo: "[P001] Teclado - 45.99 € (10 uds.) | Proveedor: TechZone (ventas@techzone.com)"
        return f"{self.codigo} {self.nombre} - {self.precio}$ ({self.stock}) | Proveedro {self.proveedor} ({self.proveedor.contacto})"

# ======================================================
# Clase Inventario
# ======================================================

class Inventario:
    def __init__(self, nombre_fichero):
        # TODO: definir los atributos e inicializar la lista de productos
        self.nombre_fichero = nombre_fichero
        self.productos = []

    def cargar(self):
        """
        Carga los datos del fichero JSON si existe y crea los objetos Producto y Proveedor.
        Si el fichero no existe, crea un inventario vacío.
        """
        # TODO: implementar la lectura del fichero JSON y la creación de objetos
        try:
            with open(self.nombre_fichero, "r", encoding="UTF-8") as fichero:
                datos = json.load(fichero)

                for p in datos:
                    self.productos.append(p)

                return print("Datos cargados")
        except FileNotFoundError :
            return []

    def guardar(self):
        """
        Guarda el inventario actual en el fichero JSON.
        Convierte los objetos Producto y Proveedor en diccionarios.
        """
        # TODO: recorrer self.productos y guardar los datos en formato JSON
        with open(self.nombre_fichero, "w", encoding="UTF-8") as fichero:
            json.dump(self.productos, fichero, indent=4)
            return print("Datos guardados")

    def anadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario si el código no está repetido.
        """
        # TODO: comprobar si el código ya existe y, si no, añadirlo
        for p in self.productos:
            if p.codigo == producto.codigo:
                self.productos.append(producto)
                return print(f"Producto {producto} añadido")
        
        return print("Producto EXISTENTE en la lista")


    def mostrar(self):
        """
        Muestra todos los productos del inventario.
        """
        # TODO: mostrar todos los productos almacenados
        for p in self.productos:
            print(str(p))

    def buscar(self, codigo):
        """
        Devuelve el producto con el código indicado, o None si no existe.
        """
        # TODO: buscar un producto por código
        for p in self.productos:
            if p['codigo'] == codigo:
                return p
        return None

    def modificar(self, codigo, nombre=None, precio=None, stock=None):
        """
        Permite modificar los datos de un producto existente.
        """
        # TODO: buscar el producto y actualizar sus atributos
        p = self.buscar(codigo)
        if p!= None:
            if(nombre!=None):
                p.nombre = nombre
            if(precio!=None):
                p.precio = precio
            if(stock!=None):
                p.stock = stock
        return "Datos modificados"
                

    def eliminar(self, codigo):
        """
        Elimina un producto del inventario según su código.
        """
        # TODO: eliminar el producto de la lista
        if self.buscar(codigo) == None:
            return "Producto no exsistente"
        else:
            self.productos.remove(self.buscar(codigo))
            return print("Producto eliminado")

    def valor_total(self):
        """
        Calcula y devuelve el valor total del inventario (precio * stock).
        
        """
        # TODO: devolver la suma total del valor del stock
        sumaTotal = 0
        for p in self.productos:
            print(p)
            sumaTotal += p['precio'] * p['stock']

        return sumaTotal

    def mostrar_por_proveedor(self, nombre_proveedor):
        """
        Muestra todos los productos de un proveedor determinado.
        Si no existen productos de ese proveedor, mostrar un mensaje.
        """
        # TODO: filtrar y mostrar los productos de un proveedor concreto
        resultado = ""
        for p in self.productos:
            if p['proveedor']['codigo'] == nombre_proveedor:
                resultado += str(p['nombre']+"\n")

        if resultado == "":
            return "Datos no encontrados"
        
        return resultado

# ======================================================
# Función principal (menú de la aplicación)
# ======================================================

def main():
    # TODO: crear el objeto Inventario y llamar a los métodos según la opción elegida


    inventario = Inventario("inventario.json")
    inventario.cargar()

    while True:
        print("\n=== GESTIÓN DE INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Mostrar inventario")
        print("3. Buscar producto")
        print("4. Modificar producto")
        print("5. Eliminar producto")
        print("6. Calcular valor total")
        print("7. Mostrar productos de un proveedor")
        print("8. Guardar y salir")

        opcion = int(input("Seleccione una opción: "))

        # TODO: implementar las acciones correspondientes a cada opción del menú
        if(opcion == 1):
            try:
                codigo = input("Introduzca el codigo del nuevo producto: ")
                nombre = str(input("Introduzca el nombre del producto: "))
                precio = int(input("Introduzca el precio del producto: "))
                stock = int(input("Introduzca el stock del producto: "))
                print("Datos PROVEEDOR")
                codProv = input("Introduzca el codigo del proveedor: ")
                nombProv = str(input("Introduzca los datos del proveedor: "))
                contacto = input("Introduzca el contacto del proveedor: ")

                proveedor = Proveedor(codProv, nombProv, contacto)
                prod = Producto(codigo, nombre, precio, stock, proveedor)
                inventario.anadir_producto(prod)

            except ValueError:
                print("Valores mal introducidos")
            except NameError as e:
                print(f"Errorm {e}")

        elif(opcion == 2):
            inventario.mostrar()

        elif(opcion == 3):
            codigo = input("Introduzca el codigo del producto a buscar: ")
            print(f"{inventario.buscar(codigo)} prodcuto ")

        elif(opcion == 4):
            codigo = input("Introduzca el codigo del nuevo producto: ")
            nombre = str(input("Introduzca el nombre del producto: "))
            precio = int(input("Introduzca el precio del producto: "))
            stock = int(input("Introduzca el stock del producto: "))

            inventario.modificar(codigo, nombre, precio, stock)

        elif(opcion == 5):
            codigo = input("Introduzca el codigo del producto a eliminar")
            print(inventario.eliminar(codigo))

        elif(opcion == 6):
            print(f"La suma total es de {inventario.valor_total()}$")

        elif(opcion ==7):
            codProv = input("Introduzca el codigo del proveedor: ")
            print(inventario.mostrar_por_proveedor(codProv))

        elif(opcion == 8):
            inventario.guardar()
            break



if __name__ == "__main__":
    main()
