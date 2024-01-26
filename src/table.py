class Seat:
    def __init__(self):
        self.free = True
        self.occupant = None
    def __str__(self):
        return f"Free Seat: {self.free} Occupant: {self.occupant}"
    
    def set_occupant(self, name):
        """
        Checks if a seat is free, and assigns an individual based on the parameter (name)
        Output will bring Assigned if successful, and Failed to assign if there is no space
        """
        if self.free == True:
            self.occupant = name
            self.free = False
            print(f"Assigned {name}")
        else:
            print(f"Failed to assign {name}")
            

    def remove_occupant(self):
        """
        If a seat is occupied, removes the occupant
        Output will print the name of occupant just removed if successful, otherwise a notice that there's no occupant
        """
        if self.free == False:
            self.old_occupant = self.occupant
            self.occupant = None
            self.free = True
            print(self.old_occupant)
        else:
            print("No occupant to remove")
            return None


class Table:
    
    def __init__(self, capacity=6):
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)]

    def __str__(self):
        print(f"Capacity = {self.capacity} Seats: {self.seats}")
    
    def has_free_spot(self): #ok
        """
        Checks if there any free seats on a given instance of Table
        """
        return any(list(seat.free for seat in self.seats))

        
    def assign_seat(self, name):
        """
        If there is an empty seat, choose it and place occupant (name) there
        """
        for seat in self.seats: # if there is an empty seat. pick and set a 
            
            if seat.free:
                 seat.set_occupant(name)
                 
                 break
        
    def capacity_check(self):
        """
        Counts how many individuals seated in a given instance of table and returns the value
        """
        return sum(1 for seat in self.seats if not seat.free)

    

        
    def capacity_left(self):
        """
        Counts how many empty seats remain in a given instance of table and returns the value
        """
        return sum(seat.free for seat in self.seats)
    

