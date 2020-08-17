class Producto():
    def __init__(self, descripcion="", precio=0, tipo=""):
        self.descripcion = descripcion
        self.precio = precio
        self.tipo = tipo

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, valor_descripcion):
        self._descripcion = valor_descripcion

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, valor_precio):
        self._precio = valor_precio

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, valor_tipo):
        self._tipo = valor_tipo
