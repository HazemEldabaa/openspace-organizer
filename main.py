from src.openspace import OpenSpace
from src.table import Table
from src.table import Seat


read = open("colleagues.txt", "r")
ready = [read.read().split()][0]


    
if __name__ == "__main__":


    open_space = OpenSpace()


    open_space.organize(ready)
    open_space.display()
    open_space.store("output.txt")
