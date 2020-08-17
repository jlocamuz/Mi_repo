from producto import Producto
from repositorios import Repositorios


class ProductoService():

    def get_productosList(self):
        return Repositorios.productosList

    def add_producto(self, producto):
        lastKey = -1
        for key in Repositorios.productosList:
            lastKey = key
        productoKey = int(lastKey) + 1
        Repositorios.productosList[productoKey] = Producto.producto.__dict__
        return productoKey

    def delete_producto(self, key_que_borrare):
        if key_que_borrare is in list(range(TestProducto.longlist):
            del(Repositorios.productosList[key_que_borrare])
        else:
            raise(ValueError)
