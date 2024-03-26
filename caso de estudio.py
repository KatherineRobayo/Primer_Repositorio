# Definimos la clase Persona
class Persona:
  def __init__(self, nombre, apellido):
    self.nombre = nombre
    self.apellido = apellido

  def get_nombre(self):
    return self.nombre

  def get_apellido(self):
    return self.apellido

# Definimos la clase Cuenta
class Cuenta:

    def __init__(self, titular, cantidad=0.0):
        """
        Crea una nueva cuenta con los datos especificados.

        Args:
            titular (Persona): El titular de la cuenta.
            cantidad (float, optional): La cantidad inicial en la cuenta. Predeterminado: 0.0.
        """
        if not isinstance(titular, Persona):
            raise TypeError("El titular debe ser una instancia de Persona")
        self.titular = titular
        self.cantidad = cantidad

    def set_titular(self, titular):
        """
        Establece el titular de la cuenta.

        Args:
            titular (Persona): El nuevo titular.
        """
        if not isinstance(titular, Persona):
            raise TypeError("El titular debe ser una instancia de Persona")
        self.titular = titular

    def set_cantidad(self, cantidad):
        """
        Establece la cantidad en la cuenta.

        Args:
            cantidad (float): La nueva cantidad.
        """
        self.cantidad = cantidad

    def get_titular(self):
        """
        Obtiene el titular de la cuenta.

        Returns:
            Persona: El titular de la cuenta.
        """
        return self.titular

    def get_cantidad(self):
        """
        Obtiene la cantidad en la cuenta.

        Returns:
            float: La cantidad en la cuenta.
        """
        return self.cantidad

    def mostrar(self):
        """
        Muestra los datos de la cuenta.
        """
        print(f"Titular: {self.titular.get_nombre()} {self.titular.get_apellido()}")
        print(f"Cantidad: {self.cantidad:.2f}")

    def ingresar(self, cantidad):
        """
        Ingresa una cantidad a la cuenta.

        Args:
            cantidad (float): La cantidad a ingresar.
        """
        if cantidad <= 0:
            print("No se puede ingresar una cantidad negativa.")
        else:
            self.cantidad += cantidad
            print(f"Se han ingresado {cantidad:.2f}€ a la cuenta.")

    def retirar(self, cantidad):
        """
        Retira una cantidad de la cuenta.

        Args:
            cantidad (float): La cantidad a retirar.
        """
        if cantidad <= 0:
            print("No se puede retirar una cantidad negativa.")
        elif cantidad > self.cantidad:
            print(f"No hay suficiente saldo para retirar {cantidad:.2f}€.")
        else:
            self.cantidad -= cantidad
            print(f"Se han retirado {cantidad:.2f}€ de la cuenta.")

# Creamos una instancia de Persona y una instancia de Cuenta
persona_ejemplo = Persona("Juan", "Perez")
cuenta_ejemplo = Cuenta(persona_ejemplo, 1000.0)

# Ejemplo de uso de los métodos
cuenta_ejemplo.mostrar()
cuenta_ejemplo.ingresar(500.0)
cuenta_ejemplo.retirar(200.0)

