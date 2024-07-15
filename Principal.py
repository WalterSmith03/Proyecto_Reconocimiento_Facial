import os

from PasswordManager import PasswordManager
from LocationManager import LocationManager
from GradeCalculator import GradeCalculator
from OddNumberPrinter import OddNumberPrinter
from Reconocimiento import FaceRecognitionSystem


os.system('cls' if os.name == 'nt' else 'clear')

password_manager = PasswordManager()
password_manager.verify_password(input("Ingresa la contraseña: "))

location_manager = LocationManager()
grade_calculator = GradeCalculator()
odd_number_printer = OddNumberPrinter()

while True:
    print("\nMenu:")
    print("1. Inspeccionar los departamentos")
    print("2. Inspeccionar los municipios")
    print("3. Calcular promedio")
    print("4. Mostrar números impares")
    print("5. Salir")
    print("")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        print("")
        departamento = input("Ingrese el nombre del departamento: ")
        if departamento in location_manager.departamentos:
            print("\nMunicipios del departamento:")
            print("")
            for municipio, codigo in location_manager.departamentos[departamento].items():
                print(f"{municipio} - {codigo}")
        else:
            print("Departamento no encontrado.")
    elif opcion == "2":
        location_manager.print_results()
    elif opcion == "3":
        grade_calculator.calculate_average()
    elif opcion == "4":
        reconociminto()
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Opcion no válida. Por favor, seleccione una opción del menú.")