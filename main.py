class Auto:

    cantidadCreados = 0
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
          self.modelo = modelo
          self.precio = precio
          self.asientos = asientos
          self.marca = marca
          self.motor = motor
          self.registro = registro

    def cantidadAsientos(self):
        contadorasientos = 0
        for Asiento in self.asientos:
            if isinstance (Asiento, self.asientos):
                contadorasientos += 1
        return contadorasientos

    def verficarIntegridad(self):

        for self.asientos in Asiento:
            if isinstance(self.asientos, Asiento):
                if self.asientos.regsistro != self.registro:
                    return "Las piezas no son originales"
        if self.motor.registro != self.registro:
            return "Las piezas no son originales"
        return "Auto original"

class Asiento:

    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        permitidos = ["rojo", "verde", "amarillo", "negro", "blanco"]

        if color in permitidos:
            self.color = color

class Motor:

    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
        
    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        tipoMotor = ["electrico", "gasolina"]

        if tipo in tipoMotor:
            self.tipo = tipo










          
             



