import os

class PasswordManager:
    def __init__(self):
        self.password = "UTH123"

    def verify_password(self, input_password):
        if input_password == self.password:
            print("Contraseña correcta. Acceso permitido.")
        else:
            print("Contraseña incorrecta. Acceso denegado.")
            exit()