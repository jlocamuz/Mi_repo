class Clase():
    def __init__(self, atributo=0):
        # Que yo ponga atributo=0 significa que si yo no le doy valor
        # A ese atributo por defecto me pone 0
        self.atributo = atributo

    def get_atributo(self):
        # setter and getter: darle un valor a un atributo y obtener
        # el valor del atributo
        return self.atributo

    def set_atributo(self, value):
        self.atributo = value


if __name__ == "__main__":
    objeto1 = Clase(1)
    objeto2 = Clase(2)
    # objeto1 = Clase(1)
    # objeto2 = Clase(2)
    # es lo mismo hacerlo con el setter y getter
    objeto1.set_atributo(1)
    objeto2.set_atributo(2)
    print(objeto1.__dict__)
    print(objeto2.__dict__)
