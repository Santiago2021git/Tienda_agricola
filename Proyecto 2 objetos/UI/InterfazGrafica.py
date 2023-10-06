from MODELO import Factura
from MODELO import Antibiotico
from MODELO import ProductoControl
from MODELO import Cliente

def inicio():
     print("Facturacion Tienda AgroPereira")

def ingreso_de_datos_cliente():
     nombre = (str(input("Ingrese el nombre del cliente: ")))
     cedula = (int(input("Ingresar el numero de cedula del cliente: ")))
     return [nombre, cedula]

def ingreso_de_datos_factura():
     fecha = (str(input("Ingrese la fecha de la factura: ")))
     return fecha

def ingreso_de_datos_antibiotico():
     nombre_del_producto = (str(input("Ingrese el nombre del producto: ")))
     dosis = (str(input("Ingrese la dosis del producto: ")))
     precio = (int(input("Ingrese ingrese el precio: ")))
     return [nombre_del_producto, dosis, precio]

def ingreso_de_datos_plaga():
     registro_ica = (str(input("Ingrese el registro ica del producto: ")))
     nombre_del_producto = (str(input("Ingrese el nombre del producto: ")))
     frecuencia_de_aplicacion = (str(input("Ingrese la frecuencia de aplicacion del producto: ")))
     valor_del_producto = (int(input("Ingrese el valor del producto: ")))
     periodo_de_carencia = (str(input("Ingrese el periodo de carencia del producto: ")))
     return [registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto, periodo_de_carencia]

def ingreso_de_datos_fertilizante():
     registro_ica = (str(input("Ingrese el registro ica del producto: ")))
     nombre_del_producto = (str(input("Ingrese el nombre del producto: ")))
     frecuencia_de_aplicacion = (str(input("Ingrese la frecuencia de aplicacion del producto: ")))
     valor_del_producto = (int(input("Ingrese el valor del producto: ")))
     fecha_de_ultima_aplicacion = (str(input("Ingrese la fecha de ultima aplicacion del producto: ")))
     return [registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto, fecha_de_ultima_aplicacion]

def imprimir(lista_Clientes):
    contador = 0
    tamaño = len(lista_Clientes)
    while contador <= tamaño - 1:
        print("      ")
        print("nombre del cliente: ", lista_Clientes[contador]._nombre)
        print("cedula: ", lista_Clientes[contador]._cedula)

        contador_2 = 0
        tamaño_factura = len(lista_Clientes[contador]._factura_cliente)
        while contador_2 <= tamaño_factura - 1:
            print("            ")
            print("Datos de la Factura")
            print("fecha de la factura: ", lista_Clientes[contador]._factura_cliente[contador_2]._fecha)
            print("valor de la compra: ", lista_Clientes[contador]._factura_cliente[contador_2]._valor_de_la_compra)
            contador_3 = 0
            contador_4 = 0
            contador_5 = 0
            tamaño_productos_antibioticos = len(lista_Clientes[contador]._factura_cliente[contador_2]._antibiotico)
            tamaño_productos_plagas = len(lista_Clientes[contador]._factura_cliente[contador_2]._plaga)
            tamaño_productos_fertilizantes = len(lista_Clientes[contador]._factura_cliente[contador_2]._fertilizante)
            while contador_3 <= tamaño_productos_antibioticos - 1:
                print("           ")
                print("antibioticos")
                print("nombre del producto: ", lista_Clientes[contador]._factura_cliente[contador_2]._antibiotico[
                    contador_3]._nombre_del_producto)
                print("dosis(entre 400kg y 600kg): ",
                      lista_Clientes[contador]._factura_cliente[contador_2]._antibiotico[contador_3]._dosis)
                print("tipo de animal: ",
                      lista_Clientes[contador]._factura_cliente[contador_2]._antibiotico[contador_3]._tipo_de_animal)
                print("precio: ",
                      lista_Clientes[contador]._factura_cliente[contador_2]._antibiotico[contador_3]._precio)
                contador_3 = contador_3 + 1
            while contador_4 <= tamaño_productos_plagas - 1:
                print("           ")
                print("productos de control : plagas")
                print("registro ica: ",
                      lista_Clientes[contador]._factura_cliente[contador_2]._plaga[contador_4]._registro_ica)
                print("nombre del producto: ",
                      lista_Clientes[contador]._factura_cliente[contador_2]._plaga[contador_4]._nombre_del_producto)
                print("frecuencia de aplicacion: ", lista_Clientes[contador]._factura_cliente[contador_2]._plaga[
                    contador_4]._frecuencia_de_aplicacion)
                print("valor del producto: ",
                      lista_Clientes[contador]._factura_cliente[contador_2]._plaga[contador_4]._valor_del_producto)
                print("periodo de carencia: ",
                      lista_Clientes[contador]._factura_cliente[contador_2]._plaga[contador_4]._periodo_de_carencia)
                contador_4 = contador_4 + 1
            while contador_5 <= tamaño_productos_fertilizantes - 1:
                print("           ")
                print("productos de control : fertilizantes")
                print("registro ica",
                      lista_Clientes[contador]._factura_cliente[contador_2]._fertilizante[contador_5]._registro_ica)
                print("nombre del producto", lista_Clientes[contador]._factura_cliente[contador_2]._fertilizante[
                    contador_5]._nombre_del_producto)
                print("frecuencia de aplicacion", lista_Clientes[contador]._factura_cliente[contador_2]._fertilizante[
                    contador_5]._frecuencia_de_aplicacion)
                print("valor del producto", lista_Clientes[contador]._factura_cliente[contador_2]._fertilizante[
                    contador_5]._valor_del_producto)
                print("fecha de ultima aplicacion: ",
                      lista_Clientes[contador]._factura_cliente[contador_2]._fertilizante[
                          contador_5]._fecha_de_ultima_aplicacion)
                contador_5 = contador_5 + 1

            contador_2 = contador_2 + 1

        contador = contador + 1


def crear_factura():
    fecha = ingreso_de_datos_factura()
    precio_factura = 0
    factura_mi_cliente = Factura.Factura(fecha)
    eleccion2 = 0
    while eleccion2 != 4:
        print("    ")
        print("1.agregar antibiotico")
        print("2.agregar producto de control para plaga")
        print("3.agregarproducto de control fertilizante")
        print("4.Salir")
        eleccion2 = (int(input("Ingrese la opcion: ")))

        if eleccion2 == 1:
            nombre_del_producto, dosis, precio = ingreso_de_datos_antibiotico()
            miantibiotico = Antibiotico.Antibiotico(nombre_del_producto, dosis, precio)
            factura_mi_cliente._antibiotico.append(miantibiotico)
            precio_factura = precio_factura + miantibiotico._precio

        if eleccion2 == 2:
            registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto, periodo_de_carencia = ingreso_de_datos_plaga()
            mi_producto_plaga = ProductoControl.Producto_Plaga(registro_ica, nombre_del_producto,
                                                               frecuencia_de_aplicacion, valor_del_producto,
                                                               periodo_de_carencia)
            factura_mi_cliente._plaga.append(mi_producto_plaga)
            precio_factura = precio_factura + mi_producto_plaga._valor_del_producto

        if eleccion2 == 3:
            registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto, fecha_de_ultima_aplicacion = ingreso_de_datos_fertilizante()
            mi_producto_fertilizante = ProductoControl.Producto_Fertilizante(registro_ica, nombre_del_producto,
                                                                             frecuencia_de_aplicacion,
                                                                             valor_del_producto,
                                                                             fecha_de_ultima_aplicacion)
            factura_mi_cliente._fertilizante.append(mi_producto_fertilizante)
            precio_factura = precio_factura + mi_producto_fertilizante._valor_del_producto
            
        if eleccion2 == 4:
            exit()

    factura_mi_cliente._valor_de_la_compra = precio_factura
    return factura_mi_cliente



def opciones():
    print("   ")
    print("1.Agregar cliente ")
    print("2.imprimir cientes ")
    print("3.agregar factura a un cliente")
    print("4.Salir ")

def crear_cliente(lista_Clientes):
    nombre, cedula = ingreso_de_datos_cliente()
    micliente = Cliente.Cliente(nombre, cedula)
    factura_mi_cliente = crear_factura()
    micliente._factura_cliente.append(factura_mi_cliente)
    lista_Clientes.append(micliente)

def agregar_factura_a_cliente(lista_Clientes):
    factura_mi_cliente = crear_factura()
    cedula = (int(input("ingrese el numero de cedula del cliente al que le va a asignar la factura: ")))
    contador_lista = 0

    while cedula != lista_Clientes[contador_lista]._cedula:
        contador_lista = contador_lista + 1

    lista_Clientes[contador_lista]._factura_cliente.append(factura_mi_cliente)