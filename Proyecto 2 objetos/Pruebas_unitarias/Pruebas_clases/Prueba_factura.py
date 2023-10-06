class Factura:
    """
    >>> factura = Factura("2023-10-06")
    >>> factura.fecha
    '2023-10-06'
    
    >>> factura.antibiotico = "Antibiótico A"
    >>> factura.antibiotico
    ['Antibiótico A']

    >>> factura.plaga = "Plaga B"
    >>> factura.plaga
    ['Plaga B']

    >>> factura.fertilizante = "Fertilizante C"
    >>> factura.fertilizante
    ['Fertilizante C']
    """

    def __init__(self, fecha):
        self._fecha = fecha
        self._valor_de_la_compra = 0
        self._antibiotico = []
        self._plaga = []
        self._fertilizante = []

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @property
    def antibiotico(self):
        return self._antibiotico

    @antibiotico.setter
    def antibiotico(self, antibiotico):
        self._antibiotico.append(antibiotico)

    @property
    def plaga(self):
        return self._plaga

    @plaga.setter
    def plaga(self, plaga):
        self._plaga.append(plaga)

    @property
    def fertilizante(self):
        return self._fertilizante

    @fertilizante.setter
    def fertilizante(self, fertilizante):
        self._fertilizante.append(fertilizante)

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
