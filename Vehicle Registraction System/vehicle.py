class Vehicle:
    def __init__(self, reg_num, type_, owner):
        self.registration_number = reg_num
        self.type_ = type_
        self.owner = owner
        
    def display_vehicle(self):
        print("Registration Number: ", self.registration_number)
        print("Type: ", self.type_)
        print("Owner: ", self.owner)