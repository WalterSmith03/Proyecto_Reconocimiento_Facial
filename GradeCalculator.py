class GradeCalculator:
    def calculate_average(self):
        calificaciones = []
        for _ in range(3):
            calificacion = float(input("Ingrese la calificación: "))
            calificaciones.append(calificacion)
        promedio = sum(calificaciones) / len(calificaciones)
        if promedio >= 95:
            print(f"El promedio es de {promedio:.2f}. Excelencia académica.")
        else:
            print(f"El promedio es de {promedio:.2f}. No es de excelencia académica.")