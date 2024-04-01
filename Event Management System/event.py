class Event:
    def __init__(self, name = "Mahrus", date="04/02/2024"):
        self.name = name
        self.date = date
        self.count = 0
    
    def add_participant(self, count = 1):
        self.count += count
            
    def remove_participant(self, count = 1):
        self.count -= count
            
    def print_participant(self):
        print(self.count)
        
        
event = Event()
event.add_participant()
event.add_participant(10)
event.add_participant()
event.print_participant()

event.remove_participant()
event.print_participant()
event.remove_participant(5)
event.print_participant()
