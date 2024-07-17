import cv2
import face_recognition as fr
import numpy as np
from datetime import datetime

class FaceRecognitionSystem:
    def __init__(self):
        self.encoded_faces = []
        self.face_names = []

    def add_face(self, image, name):
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        encodings = fr.face_encodings(rgb_image)[0]
        self.encoded_faces.append(encodings)
        self.face_names.append(name)

    def take_photo(self):
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        success, img = cap.read()
        cap.release()
        if not success:
            raise Exception("No se pudo tomar la foto")
        return img

    def recognize_face(self, img):
        face_locations = fr.face_locations(img)
        face_encodings = fr.face_encodings(img, known_face_locations=face_locations)
        return face_locations, face_encodings

    def find_matches(self, face_encodings):
        matches = []
        distances = []
        for encoding in face_encodings:
            match = fr.compare_faces(self.encoded_faces, encoding, 0.6)
            distance = fr.face_distance(self.encoded_faces, encoding)
            matches.append(match)
            distances.append(distance)
        return matches, distances

    def get_best_match_index(self, distances):
        if len(distances) > 0:
            return np.argmin(distances)
        return None

    def draw_circle_and_timestamp(self, img, face_location):
        top, right, bottom, left = face_location
        center_x, center_y = (left + right) // 2, (top + bottom) // 2
        radius = (right - left) // 2
        cv2.circle(img, (center_x, center_y), radius, (0, 255, 0), 2)

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cv2.putText(img, timestamp, (10, img.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    def run(self):
        img = self.take_photo()
        face_locations, face_encodings = self.recognize_face(img)

        if len(face_encodings) == 0:
            print("No faces found")
            return

        matches, distances = self.find_matches(face_encodings)
        best_match_index = self.get_best_match_index(distances[0])

        if best_match_index is not None and distances[0][best_match_index] < 0.6:
            name = self.face_names[best_match_index]
            print(f"Welcome {name}")
            self.draw_circle_and_timestamp(img, face_locations[0])
        else:
            print("No match found")
            self.draw_circle_and_timestamp(img, face_locations[0])

        cv2.imshow("Employee Photo", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# Ejemplo de uso de la clase
frs = FaceRecognitionSystem()

# Agregar manualmente rostros conocidos
# Por ejemplo:
# imagen = cv2.imread("ruta/a/la/imagen.jpg")
# frs.add_face(imagen, "Nombre del Empleado")

# Ejecutar el sistema
frs.run()