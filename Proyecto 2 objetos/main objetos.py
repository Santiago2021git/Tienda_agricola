from UI import InterfazGrafica


InterfazGrafica.inicio()
lista_Clientes = []
eleccion = 0

while eleccion != 4:
    InterfazGrafica.opciones()
    eleccion = (int(input("Ingrese la opcion: ")))

    if eleccion == 1:
        InterfazGrafica.crear_cliente(lista_Clientes)

    if eleccion == 2:
        InterfazGrafica.imprimir(lista_Clientes)

    if eleccion == 3:
        InterfazGrafica.agregar_factura_a_cliente(lista_Clientes)




