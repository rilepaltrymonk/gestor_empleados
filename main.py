
import json

from empleado import Empleado

ARCHIVO_EMPLEADOS = 'empleados.json'

class GestorEmpleado:

    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.empleados = []

    def guardar(self):
        datos = []
        for empleado in self.empleados:
            datos.append(empleado.a_diccionario())
        with open(self.nombre_archivo, 'w', encoding = 'UTF-8') as archivo:
            json.dump(datos, archivo, ensure_ascii = False)

    def cargar(self):

        try:
            with open(self.nombre_archivo, 'r', encoding = 'UTF-8') as archivo:
                datos = json.load(archivo)
        except (FileNotFoundError, json.JSONDecodeError):
            self.empleados = []
            return
        if not isinstance(datos, list):
            self.empleados = []
            return
        self.empleados = [Empleado.desde_diccionario(e) for e in self.empleados]

    def verificar_numero(self, numero):
        if len(self.empleados) == 0:
            raise ValueError('No hay empleados')
        if not 1 <= numero <= len(self.empleados):
            raise ValueError(f'Tiene que ser un numero entre el 1 y el {len(self.empleados)}')

    def agregar(self, nombre, departamento):
        nombre = nombre.strip()
        departamento = departamento.strip()
        if not nombre:
            raise ValueError('El nombre no puede estar vacio')
        if not departamento:
            raise ValueError('El departamento no puede estar vacio')
        self.empleados.append(Empleado(nombre, departamento))
        self.guardar()

    def modificar(self, numero):
        self.verificar_numero(numero)
        self.empleados[numero - 1].dar_baja()
        self.guardar()

    def eliminar(self, numero):
        self.verificar_numero(numero)
        self.empleados.pop(numero - 1)
        self.guardar()

    def ver(self):
        return self.empleados


gestor = GestorEmpleado(ARCHIVO_EMPLEADOS)
gestor.cargar()

def mostrar_menu():
    while True:
        try:
            opcion = int(input('Elige la opcion deseada:\n' \
            '1. Agregar empleado\n' \
            '2. Modificar estado del empleado\n' \
            '3. Eliminar empleado de la lista\n' \
            '4. Ver empleados actuales\n' \
            '5. Resumen\n' \
            '6. Salir\n'))
        except ValueError:
            print('Debes ingresar un numero, no una letra')
        else:
            if 1 <= opcion <= 6:
                return opcion
            print('Debes ingresar un numero entre el 1 y el 6')

def pedir_numero(mensaje):
    try:
        return int(input(mensaje))
    except ValueError:
        print('Debe ser un numero no una letra')

def opcion_agregar(gestor):
    nombre = input('Ingresa el nombre de tu nuevo empleado')
    departamento = input('Ingresa el departamento')
    try:
        gestor.agregar(nombre, departamento)
        print('Empleado agregado')
    except ValueError as error:
        print(error)

def opcion_modificar(gestor):
    numero = pedir_numero('Ingresar el numero de empleado a dar de baja')
    if numero is None:
        return 
    try:
        gestor.modificar(numero)
        print('Empleado inactivo')
    except ValueError as error:
        print(error)

def opcion_eliminar(gestor):
    numero = pedir_numero('Ingresa el numero de empleado a eliminar')
    if numero is None:
        return
    try:
        gestor.eliminar(numero)
        print('Empleado eliminado')
    except ValueError as error:
        print(error)

def opcion_ver(gestor):
    empleados = gestor.ver()
    if len(empleados) == 0:
        print('No hay empleados en la lista')
    for i, empleado in enumerate(empleados, start = 1):
        print(i, empleado)

while True:

    opcion = mostrar_menu()

    if opcion == 1:
        opcion_agregar(gestor)
    elif opcion == 2:
        opcion_modificar(gestor)
    elif opcion == 3:
        opcion_eliminar(gestor)
    elif opcion == 4:
        opcion_ver(gestor)
    elif opcion == 5:
        opcion_ver(gestor)
    elif opcion == 6:
        print('Nos vemos...')
        break