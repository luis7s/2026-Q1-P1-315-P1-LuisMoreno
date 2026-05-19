
"""
============================== SUPERMERCADO PYTHON MARKET ============================== 
1. Cargar producto 
2. Mostrar productos 3. 
Buscar producto por código 
4. Ordenar productos por precio 
5. Mostrar producto con menor stock 
6. Calcular valor total del inventario 
7. Salir

"""



lista_codigo_producto = []
lista_nombre_producto = []
lista_precio= []
lista_cantidad = []

opcion = 0



while opcion != 7:

    print("\n===== SUPERMERCADO PYTHON MARKET =====")
    print("1. Cargar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto por código ")
    print("4. Ordenar productos por precio")
    print("5. Mostrar producto con menor stock")
    print("6. Calcular valor total del inventario ")
    print("7. Salir")

    opcion = int(input("Ingrese opción: "))

    match opcion:

        case 1:

                igual = False

                codigo_producto = input("Ingrese Codigo del producto: ")
                
                
                while igual == False:
                
                    for i in range(len(lista_codigo_producto)):
                        if codigo_producto == lista_codigo_producto[i]:
                            igual = True
                            print("Codigo repetido")
                        
                    
                    if igual == True:
                        codigo_producto = input("Reingrese Codigo del producto: ")
                    else:
                        break
                    
                    
                   
                nombre_producto = input("Ingrese nombre del producto: ")
                
                
                while nombre_producto == " ":
                    nombre_producto = input("Ingreso un espacio. Reingrese nombre del producto: ")
                
                precio = float(input("Ingrese el precio: "))

                while precio <= 0:
                    precio = float(input("No se permite precios menores o iguales a 0. Reingrese el precio: "))
                    
                    
                cantidad = int(input("Ingrese la cantidad: "))
                
                
                while cantidad < 0:
                    
                    cantidad = int(input("No se permite numeros negativos. Reingrese la cantidad: "))
                
                lista_codigo_producto.append(codigo_producto)
                lista_nombre_producto.append(nombre_producto)
                lista_precio.append(precio)
                lista_cantidad.append(cantidad)

                print("Agregrado")
                
        case 2:

                if len(lista_codigo_producto) > 0:

                    for i in range(len(lista_codigo_producto)):

                        print("\n----------------")
                        print("Codigo:", lista_codigo_producto[i])
                        print("Nombre Producto:", lista_nombre_producto[i])
                        print("Precio:", lista_precio[i])
                        print("Cantidad:", lista_cantidad[i])
                else:
                    print("No hay productos")

        case 3:
                buscar = input("Ingrese codigo a buscar: ")

                encontrado = False

                for i in range(len(lista_codigo_producto)):

                    if lista_codigo_producto[i].lower() == buscar.lower():

                        print("\nProducto encontrado")
                        print("Codigo:", lista_codigo_producto[i])
                        print("Nombre Producto:", lista_nombre_producto[i])
                        print("Precio:", lista_precio[i])
                        print("Cantidad:", lista_cantidad[i])

                        encontrado = True

                if encontrado == False:
                    print("Libro no encontrado")
                        
        case 4:

                for i in range(len(lista_precio)):
        
                    for j in range(len(lista_precio)-1):
                        
                        if lista_precio[j] > lista_precio[j +1]:
                                auxiliar = lista_precio[j]
                                lista_precio[j] = lista_precio[j+1]
                                lista_precio [j+1] = auxiliar
                
                print("Ordenado por precio de menor a mayor: Ingrese 2 para ver")
                
        case 5:
                minimo = 0
                bandera = False
                for i in range(len(lista_nombre_producto)):
                    if lista_cantidad[i] < minimo or bandera == False:
                        minimo = lista_cantidad[i]
                        nombre_menor_stock = lista_nombre_producto[i]
                        bandera = True
                        
                print(f"El producto con menor stock es {nombre_menor_stock} y la cantidad es {minimo}")
                
        case 6:
                total = 0
                
                for i in range(len(lista_codigo_producto)):
                    precio = lista_cantidad[i] * lista_precio[i]
                    print(f"El precio de {lista_nombre_producto[i]} es {precio}")
                    total += precio
                
                print("Cantidad sumando todos los productos: ",total)

        case 7:
            print("Ha salido del programa!!")

        case _:
            print("Opción inválida")
            
        
    
    