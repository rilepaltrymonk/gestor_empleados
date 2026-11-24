class Empleado:

    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento
        self.status = True

    def __str__(self):
        if self.status:
            return f'{self.nombre}-{self.departamento}-Activo'
        else:
            return f'{self.nombre}-{self.departamento}-Inactivo'

    def dar_baja(self):
        self.status = False

    def a_diccionario(self):
        return {'nombre': self.nombre, 'departamento': self.departamento, 'status': self.status}

    @classmethod
    def desde_diccionario(cls, datos):
        nuevo = cls(datos['nombre'])
        nuevo.departamento = datos['departamento']
        nuevo.status = datos['status']
