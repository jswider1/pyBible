# coins, working with class / objects
import random

# to use classes type for example:
# one_dollar_coin = Dollar() ### this creates an instance of Dollar with Coin attributes
# one_dollar_coin.color   ### this will check the Dollar coin color
# one_dollar_coin.rust()  ### calls the rust function and changes the coin color
class Coin:
    # constructor "initiate" , keywordarguments kwargs data packing
    def __init__(self, rare=False, clean=True, heads = True,**kwargs):

        for key,value in kwargs.items():
            # set attributes
            setattr(self,key,value)
        
        self.is_rare = rare # self refers to an instance of class
        self.is_clean = clean # simplifying variable names
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.color = self.clean_color
        else:
            self.color = self.rusty_color

    def rust(self):
        self.color = self.rusty_color

    def clean(self):
        self.color = self.clean_color
        
    # destructor "delete"
    def __del__(self):
        print("Coin Spent")

    def flip(self):
        heads_options = [True,False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __str__(self):
        if self.original_value >= 1.00:
            return "${} coin".format(int(self.original_value))
        else:
            return "{}c coin".format(int(self.original_value *100))

# Dollar inherit from Coin
class Dollar(Coin):
    def __init__(self):
        data ={
            "original_value":1.00,
            "clean_color":"silver",
            "rusty_color":"greenish",
            "diameter":35,
            "thickness":3.15,
            "mass":9.5
            }
        super().__init__(**data) # data packaging

class Penny(Coin):
    def __init__(self):
        data ={
            "original_value":0.01,
            "clean_color":"copper",
            "rusty_color":"greenish",
            "diameter":15,
            "thickness":2.8,
            "mass":3.2
            }
        super().__init__(**data)

class Dime(Coin):
    def __init__(self):
        data ={
            "original_value":0.10,
            "clean_color":"silver",
            "rusty_color":"greenish",
            "diameter":13,
            "thickness":2.2,
            "mass":2.5
            }
        super().__init__(**data)
    # polymorphism - has multiple forms for itself
    def rust(self):
        self.color = self.clean_color
        
class Nickle(Coin):
    def __init__(self):
        data ={
            "original_value":0.05,
            "clean_color":"silver",
            "rusty_color":"greenish",
            "diameter":20,
            "thickness":2.5,
            "mass":3.8
            }
        super().__init__(**data)

class Half_Dollar(Coin):
    def __init__(self):
        data ={
            "original_value":0.50,
            "clean_color":"silver",
            "rusty_color":"greenish",
            "diameter":25,
            "thickness":2.9,
            "mass":5.5
            }
        super().__init__(**data)

class Quarter(Coin):
    def __init__(self):
        data ={
            "original_value":0.25,
            "clean_color":"silver",
            "rusty_color":"greenish",
            "diameter":22.5,
            "thickness":2.8,
            "mass":4.9
            }
        super().__init__(**data)
        
coins = [Penny(), Nickle(), Dime(), Quarter(), Half_Dollar(), Dollar()]

for coin in coins:
    arguments = [coin,coin.color,coin.value,coin.diameter,coin.thickness,coin.mass]
# unpacking arguments *arguments
    string = "{} - Color: {}, value: {}, diameter: {}, thickness: {}, mass: {}".format(*arguments)
    print(string)
    
