class Antibiotico:
    """
    Esta clase representa un antibiótico.

    >>> antibiotico = Antibiotico("Antibiótico A", "10 mg", 20.0)
    >>> antibiotico.nombre_del_producto
    'Antibiótico A'
    >>> antibiotico.dosis
    '10 mg'
    >>> antibiotico.precio
    20.0

    >>> antibiotico.nombre_del_producto = "Nuevo Antibiótico"
    >>> antibiotico.nombre_del_producto
    'Nuevo Antibiótico'

    >>> antibiotico.dosis = "5 mg"
    >>> antibiotico.dosis
    '5 mg'

    >>> antibiotico.precio = 25.0
    >>> antibiotico.precio
    25.0
    """

    def __init__(self, nombre_del_producto, dosis, precio):
        self._nombre_del_producto = nombre_del_producto
        self._dosis = dosis
        self._precio = precio

    @property
    def nombre_del_producto(self):
        return self._nombre_del_producto

    @nombre_del_producto.setter
    def nombre_del_producto(self, nombre_del_producto):
        self._nombre_del_producto = nombre_del_producto

    @property
    def dosis(self):
        return self._dosis

    @dosis.setter
    def dosis(self, dosis):
        self._dosis = dosis

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        self._precio = precio

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
