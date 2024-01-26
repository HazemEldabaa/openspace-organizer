
import random
from src.table import Table 

class OpenSpace:
    """
    Creates an openspace with tables and seats to assign individuals
    Parameters are intialized at 4 tables and 6 seats

    """
    
    def __init__(self, number_of_tables=4, table_capacity=6):
        self.tables = [Table(table_capacity) for _ in range(number_of_tables)]
        self.number_of_tables = number_of_tables
        self.table_capacity=table_capacity
    
    def __str__(self):
        return f"OpenSpace with {self.number_of_tables} tables and {self.table_capacity} seats"
    
    def organize(self, names):

        """
        Randomly assigns individuals on an empty seat at an available table
        """

        total_capacity = self.number_of_tables*self.table_capacity

        if len(names) > total_capacity:
            raise ValueError("Too many people for the available seats.")
        
        for table in self.tables:
            for seat in table.seats:
                if table.has_free_spot():
                    name = random.choice(names)
                    #for name in names:
                    
                    table.assign_seat(name)
                        #store.remove(name)
                    names.remove(name)
                        #print(store)
                else:
                    print(f"No available seat for {name}.")
                    continue
            
                    """break
            if not assigned:
                print(f"No available seat for {name}. Some people may not be seated.")"""""

    def display(self):
        """
        Displays the tables and their occupants in a structured format
        """
        print(f"Open Space Seating Arrangement:\n Number of people in the room: {sum(table.capacity_check() for table in self.tables)}\n")
        for i, table in enumerate(self.tables, start=1):
            print(f"\nTable {i} (Capacity: {table.capacity_left()} seats left):")
            for j, seat in enumerate(table.seats, start=1):
                print(f"  Seat {j}: {seat.occupant if not seat.free else 'Empty'}")
        

    def store(self, filename):
        """
        Stores the output of display in a txt file in the main directory
        """
        with open(filename, 'w') as file:
            file.write(f"Open Space Seating Arrangement:\n Number of people in the room: {(table.capacity_check() for table in self.tables)}\n")
            for i, table in enumerate(self.tables, start=1):
                file.write(f"\nTable {i} (Capacity: {table.capacity_left()} seats left):\n")
                for j, seat in enumerate(table.seats, start=1):
                    file.write(f"  Seat {j}: {seat.occupant if not seat.free else 'Empty'}\n")