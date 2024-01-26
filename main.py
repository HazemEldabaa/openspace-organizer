from src.openspace import OpenSpace
from src.table import Table
from src.table import Seat
import pandas as pd

read = open("colleagues.txt", "r")
ready = [read.read().split()][0]


    
if __name__ == "__main__":
    number_of_tables = 6
    table_capacity = 4

open_space = OpenSpace()


open_space.organize(ready)
open_space.display()

