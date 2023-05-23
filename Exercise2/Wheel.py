import random

class Wheel:
    current_face = None
    def __init__(self, faces=None):
        if faces is None:
            faces = []
        else:
            self.faces = faces
    
    def spin(self):
        self.current_face = random.choice(self.faces)

    def number_of_faces(self):
        return len(self.faces)
    
    def current_face_index(self):
        return faces.index(self.current_face)

    def __str__(self):
        if self.current_face is None:
            raise Exception("Wheel must be spinned first")
        return self.current_face
    
class SlotMachine:

    wheels = []
    def __init__(self, number_of_wheels, faces):
        if number_of_wheels > 0:
            for _ in range(number_of_wheels):
                self.wheels.append(Wheel(faces))

    def spin_wheels(self):
        for wheel in self.wheels:
            wheel.spin()
            print(wheel)


faces = ['1','2','3','4']
slot_machine = SlotMachine(3,faces)
slot_machine.spin_wheels()
