class Producto_Control:
    """
    >>> producto_control = Producto_Control("123-ICA", "Control A", "Quincenal", 15.0)
    >>> producto_control.registro_ica
    '123-ICA'
    >>> producto_control.nombre_del_producto
    'Control A'
    >>> producto_control.frecuencia_de_aplicacion
    'Quincenal'
    >>> producto_control.valor_del_producto
    15.0

    >>> producto_control.registro_ica = "456-ICA"
    >>> producto_control.registro_ica
    '456-ICA'

    >>> producto_control.nombre_del_producto = "Nuevo Control"
    >>> producto_control.nombre_del_producto
    'Nuevo Control'

    >>> producto_control.frecuencia_de_aplicacion = "Semanal"
    >>> producto_control.frecuencia_de_aplicacion
    'Semanal'

    >>> producto_control.valor_del_producto = 20.0
    >>> producto_control.valor_del_producto
    20.0
    """

    def __init__(self, registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto):
        self._registro_ica = registro_ica
        self._nombre_del_producto = nombre_del_producto
        self._frecuencia_de_aplicacion = frecuencia_de_aplicacion
        self._valor_del_producto = valor_del_producto

    @property
    def registro_ica(self):
        return self._registro_ica

    @registro_ica.setter
    def registro_ica(self, registro_ica):
        self._registro_ica = registro_ica

    @property
    def nombre_del_producto(self):
        return self._nombre_del_producto

    @nombre_del_producto.setter
    def nombre_del_producto(self, nombre_del_producto):
        self._nombre_del_producto = nombre_del_producto

    @property
    def frecuencia_de_aplicacion(self):
        return self._frecuencia_de_aplicacion

    @frecuencia_de_aplicacion.setter
    def frecuencia_de_aplicacion(self, frecuencia_de_aplicacion):
        self._frecuencia_de_aplicacion = frecuencia_de_aplicacion

    @property
    def valor_del_producto(self):
        return self._valor_del_producto

    @valor_del_producto.setter
    def valor_del_producto(self, valor_del_producto):
        self._valor_del_producto = valor_del_producto


class Producto_Plaga(Producto_Control):
    """
    >>> producto_plaga = Producto_Plaga("789-ICA", "Plaga X", "Mensual", 25.0, 10)
    >>> producto_plaga.registro_ica
    '789-ICA'
    >>> producto_plaga.nombre_del_producto
    'Plaga X'
    >>> producto_plaga.frecuencia_de_aplicacion
    'Mensual'
    >>> producto_plaga.valor_del_producto
    25.0
    >>> producto_plaga.periodo_de_carencia
    10

    >>> producto_plaga.registro_ica = "101-ICA"
    >>> producto_plaga.registro_ica
    '101-ICA'

    >>> producto_plaga.nombre_del_producto = "Nueva Plaga"
    >>> producto_plaga.nombre_del_producto
    'Nueva Plaga'

    >>> producto_plaga.frecuencia_de_aplicacion = "Quincenal"
    >>> producto_plaga.frecuencia_de_aplicacion
    'Quincenal'

    >>> producto_plaga.valor_del_producto = 30.0
    >>> producto_plaga.valor_del_producto
    30.0

    >>> producto_plaga.periodo_de_carencia = 15
    >>> producto_plaga.periodo_de_carencia
    15
    """

    def __init__(self, registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto, periodo_de_carencia):
        self._periodo_de_carencia = periodo_de_carencia
        super().__init__(registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto)

    @property
    def periodo_de_carencia(self):
        return self._periodo_de_carencia

    @periodo_de_carencia.setter
    def periodo_de_carencia(self, periodo_de_carencia):
        self._periodo_de_carencia = periodo_de_carencia


class Producto_Fertilizante(Producto_Control):
    """

    >>> producto_fertilizante = Producto_Fertilizante("111-ICA", "Fertilizante Y", "Anual", 40.0, "2023-01-01")
    >>> producto_fertilizante.registro_ica
    '111-ICA'
    >>> producto_fertilizante.nombre_del_producto
    'Fertilizante Y'
    >>> producto_fertilizante.frecuencia_de_aplicacion
    'Anual'
    >>> producto_fertilizante.valor_del_producto
    40.0
    >>> producto_fertilizante.fecha_de_ultima_aplicacion
    '2023-01-01'

    >>> producto_fertilizante.registro_ica = "222-ICA"
    >>> producto_fertilizante.registro_ica
    '222-ICA'

    >>> producto_fertilizante.nombre_del_producto = "Nuevo Fertilizante"
    >>> producto_fertilizante.nombre_del_producto
    'Nuevo Fertilizante'

    >>> producto_fertilizante.frecuencia_de_aplicacion = "Semestral"
    >>> producto_fertilizante.frecuencia_de_aplicacion
    'Semestral'

    >>> producto_fertilizante.valor_del_producto = 50.0
    >>> producto_fertilizante.valor_del_producto
    50.0

    >>> producto_fertilizante.fecha_de_ultima_aplicacion = "2023-02-01"
    >>> producto_fertilizante.fecha_de_ultima_aplicacion
    '2023-02-01'
    """

    def __init__(self, registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto, fecha_de_ultima_aplicacion):
        self._fecha_de_ultima_aplicacion = fecha_de_ultima_aplicacion
        super().__init__(registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto)

    @property
    def fecha_de_ultima_aplicacion(self):
        return self._fecha_de_ultima_aplicacion

    @fecha_de_ultima_aplicacion.setter
    def fecha_de_ultima_aplicacion(self, fecha_de_ultima_aplicacion):
        self._fecha_de_ultima_aplicacion = fecha_de_ultima_aplicacion


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
