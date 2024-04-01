from vehicle import Vehicle

def update_owner():
    reg_num = input("Enter the registration number of the vehicle: ")
    type_ = input("Enter the type of the vehicle: ")
    owner = input("Enter the owner of the vehicle: ")
    vehicle = Vehicle(reg_num, type_, owner)
    vehicle.display_vehicle()
    
Vehicle("KA01HG1234", "Car", "John Doe").display_vehicle()
Vehicle("KA01HG5678", "Bike", "Jane Doe").display_vehicle()
Vehicle("KA01HG8765", "Truck", "John Smith").display_vehicle()    
update_owner()