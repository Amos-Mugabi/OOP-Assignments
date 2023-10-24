# Practical Task: Design a class with private attributes and provide public methods to manipulate them.


class Continent:

    # Constructor to initialize private attributes: name and location

    def __init__(self, name, location):
        self.__name = name
        self.__location = location
        

    def region(self):
        print("My region is East Africa")


    # Public method to set the country (nation) name
    # Private attribute: nation

    def country(self, nation):
        self.__nation = nation

        
    # Public method to get the continent's location

    def get_location(self):
        return self.__location

# Public method to set the continent's location

    def set_location(self, location):
        self.__location = location
        return self.__location

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
        return self.__name

    def get_nation(self):
        return self.__nation

    def set_nation(self, nation):
        self.__nation = nation
        return self.__nation


# Creating an instance of the Continent class
con = Continent("Africa", "South")

# Setting the country (nation) name
con.set_nation("Uganda")

# Printing continent information
print("My Continent is ", con.get_name(), "and it is located in the ", con.get_location(), "of the Globe.")

# Calling the region method
con.region()
 
print("And my Country is ", con.get_nation())


