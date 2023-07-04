import random

class Wheel:
    current_face = None
    def __init__(self, faces):
        if len(faces) < 1 or faces is None:
            raise Exception("Faces list must be greather than 0")
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
        return f"[{self.current_face}]"
    
class SlotMachine:

    wheels = []
    current_faces = []
    def __init__(self, number_of_wheels, faces):
        self.numer_of_wheels = number_of_wheels
        if number_of_wheels > 0:
            for _ in range(number_of_wheels):
                self.wheels.append(Wheel(faces))
        
    def spin_wheels(self):
        self.current_faces = []
        for wheel in self.wheels:
            wheel.spin()
            self.current_faces.append(wheel.current_face)
    
    def payout(self):
        payout_value = 0
        for face in self.wheels[0].faces:
            count = self.current_faces.count(face)
            if count - 1 > payout_value:
                payout_value = count - 1
        return payout_value
    
    def __str__(self):
        faces = ""
        for wheel in self.wheels:
            faces += f"{wheel.__str__()} "
        return faces
    
    def histogram(self):
        list_payout = [0] * (self.numer_of_wheels)
        # print(list_payout)
        for _ in range(1000000):
            payout = 0
            self.spin_wheels()
            # print(slot_machine)
            payout = self.payout()
            # print(payout)
            list_payout[payout] += 1
        print(list_payout)




faces = ['1','2','3','4','5','6']
# faces = []
slot_machine = SlotMachine(12,faces)
# slot_machine.spin_wheels()
# print(slot_machine)
# print(slot_machine.payout())
slot_machine.histogram()
