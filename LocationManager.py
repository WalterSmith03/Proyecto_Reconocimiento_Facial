class LocationManager:
    def __init__(self):
        self.departamentos = {
            "Choluteca": {
                "Choluteca": "0601",
                "Apacilagua": "0602",
                "Concepcion de Maria": "0603",
                "Duyure": "0604",
                "El Corpus": "0605",
                "El Triunfo": "0606",
            },
            "Islas De La Bahía": {
                "Roatán": "1101",
                "Guanaja": "1102",
                "José Santos Guardiola": "1103",
                "Utila": "1104",
            },
        }

    def get_municipality_name(self, dni):
        codigo_municipio = dni[:4]
        for departamento, municipios in self.departamentos.items():
            for municipio, codigo in municipios.items():
                if codigo == codigo_municipio:
                    return municipio

    def calculate_age(self, dni):
        return 2024 - int(dni[4:8])

    def print_results(self):
        nombre = input("Por favor ingresar el nombre del ciudadano: ")
        print("")
        dni = input("Ingrese su código de DNI: ")

        municipio = self.get_municipality_name(dni)
        edad = self.calculate_age(dni)

        print("")
        print(f"El nombre del ciudadano es: {nombre}")
        print(f"El DNI ingresado corresponde al municipio de: {municipio}")
        print(f"Edad: {edad} años")
        print("")