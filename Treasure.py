import random #Import the mathematical random function to obtain random numbers

treasures = ["armor", "weapon", "food", "gold"] #Define the categories of treasures

foods = [("apple", 3), ("mutton", 5), ("cabbage", 2)] #Define the types of food

weapons = [("sword", 5), ("knife", 2), ("spear", 7)] #Define the types of weapons

class Treasure (object): #Define the treasure class
    
    def __init__ (self, aspect): #Define the initial function
        
        self.__aspect = aspect #Define the aspect of a given subject
        
        self.__carried = False #Define the state of the subject not being acquired
        
        self.__location = (-1, 1) #Define the initial location of the subject
        
        if aspect == "armor": #If the subject is an armor
            
            self.__ac = random.radiant (1, 11) #Assign the armor a random ac between 1 and 11
            
            self.__value = 20 * self.__ac #Define the value of the armor relative to its ac
            
            self.__worn = False #Define the state of the armor not being worn
            
            self.__description = "armor" #Define a basic description of the armor
            
        elif aspect == "weapon": #If the subject is a weapon
            
            weapon_aspect = random.randint (0, len(weapons) - 1) #Assign the weapon a random number between 0 and the numerical value of its type to define its type
            
            self.__attack = weapons [weapon_aspect] [1] #Define the attack strength of the weapon
            
            self.__value = 10 * self.__attack #Define the value of the weapon relative to its attack strength
            
            self.__equipped = False #Define the state of the weapon not being equipped
            
            self.__description = weapons [weapon_aspect] [0] #Define a basic description of the weapon determined by its type
            
        elif aspect == "food": #If the subject is food
            
            food_aspect = random.randint (0, len(food_aspect) - 1) #Assign the food a random number between 0 and the numerical value of its type to define its type
            
            self.__health = foods [food_aspect] [1] #Define the health value of the food relative to its type
            
            self.__value = 2 * self.__health #Define the value of the food relative to its health value
            
            self.__description = foods [food_aspect] [0] #Define a basic description of the food determined by its type
            
        elif aspect == "gold": #If the subject is an amount of gold
            
            self.__description = "some gold" #Define a basic description of the gold
            
            self.__value = random.randint (1, 30) #Assign the gold a random number between 1 and 30 to determine its value
            
    def __str__ (self): #Define the string function to describe the subject
        
        out_str = "Error" #Define the inital output in order to account for errors
        
        if self.__aspect == "armor": #If the subject is an armor
            
            out_str = self.__description + " is worth " + str(self.__value) + " coins." #Return a string describing the armor and its worth
            
        elif self.__aspect == "weapon": #If the subject is a weapon
            
            out_str = self.__description + " is worth " + str(self.__value) + " coins." #Return a string describing the weapon and its worth
            
        elif self.__aspect == "food": #If the subject is food
            
            out_str = self.__description + " is worth " + str(self.__value) + " coins." #Return a string describing the food and its worth
            
        elif self.__aspect == "gold": #If the subject is gold
            
            out_str = str(self.__value) + " coins." #Return a string that describes the amount of gold coins
            
        return out_str #Return the result
    
    def set_location (self, row, collumn): #Define a given location for the subject in terms of rows and collumns
        
        self.__location = (row, collumn) #Describe a location for the subject in terms of rows and collumns
        
    def set_location (self, location): #Define a given location for the subject in terms of a pre-established location
        
        self.__location = location #Describe the location of the subject
        
    def get_location (self): #Define the function to obtain the location of the subject
        
        return self.__location #Return the location of the subject
    
    def acquire (self): #Define the ability to acquire the subject
        
        self.__carried = True #Describe the subject being carried
        
    def drop (self, location): #Define the ability to drop the subject
        
        self.__carried = False #Describe the subject being dropped in terms of its status as carried
        
        set_location(location) #Define the location of where the subject is dropped
