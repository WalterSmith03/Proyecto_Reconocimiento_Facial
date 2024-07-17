import math

class Figura:
  def __init__(self, tipo_figura):
    self.tipo_figura = tipo_figura

  def area(self):
    if self.tipo_figura == "circulo":
      radio = float(input("Ingrese el radio del círculo: "))
      return math.pi * radio ** 2
    elif self.tipo_figura == "esfera":
      radio = float(input("Ingrese el radio de la esfera: "))
      return 4 * math.pi * radio ** 2 / 3
    else:
      print("Figura no válida.")
      return None

  def volumen(self):
    if self.tipo_figura == "esfera":
      radio = float(input("Ingrese el radio de la esfera: "))
      return (4 * math.pi * radio ** 3) / 3
    else:
      print("La figura no tiene volumen.")
      return None

figura1 = Figura("circulo")
print(f"El área del círculo es: {figura1.area()}")

figura2 = Figura("esfera")
print(f"El área de la esfera es: {figura2.area()}")
print(f"El volumen de la esfera es: {figura2.volumen()}")
