# This project would be a great way to learn about Object-Oriented Programming
# (OOP): https://en.wikipedia.org/wiki/Object-oriented_programming
# Object-Oriented Programming allows us to create our own data "types" that
# contain other data, called fields, inside them. They are like a big container.
# They also have functions, called methods, inside of them! If you remember
# working with the Finch Robots, we created a variable (bird) of type
# Finch. The Finch is a class, and the functions that we used, like
# bird.setMove(), were methods of the Finch class. Those methods
# belong to the specific instance of the class, called an object, that you
# create. In this case, bird was an object of class Finch.


# Here is an example of a class we can use for your game:
# Import deepcopy to make "deep" copies of dictionaries.
# Deep copies copy all data, whereas shallow copies make
# references to that data. To see why we might avoid this,
# read this Q&A on StackOverflow:
# https://stackoverflow.com/questions/35488769/what-is-an-object-reference-in-python
from copy import deepcopy
# I like to type-hint my Python, so it's more clear what data types certain
# variables are, or what types functions work with. Read more here:
# https://docs.python.org/3/library/typing.html
# https://peps.python.org/pep-0484/
from typing import Dict, Optional

# Create a Node class so that we can travel between "rooms" easier.
class Node:

    def __init__(self, description: str, options:Optional[Dict[str, "Node"]]=None):
        self.description = description
        if options is None:
            # The __ makes this field private. That means
            # that only the specific instance of the Node class
            # that has this variable can use this variable.
            self.__options: Dict[str, "Node"] = {}
        else:
            self.__options: Dict[str, "Node"] = deepcopy(options)
        self.__connections = {"north": None, "east": None, "west": None, "south": None}
    
    # A property is a function that acts like a field member.
    # This way, we can make some things read-only, or do special
    # conversions before returning that data.
    # Read more: https://docs.python.org/3/library/functions.html#property
    @property
    def options(self) -> Dict[str, "Node"]:
        return deepcopy(self.__options)

    # Add set and add node methods to help build our map.
    def set_interaction(self, command, action):
        self.__options[command] = action
    
    def add_interaction(self, command, action):
        # Throwing errors is a great way to handle something
        # unexpected happening, like if someone tries to add
        # an option to a node that already exists. Read more:
        # https://docs.python.org/3/tutorial/errors.html
        if option in self.__options:
            raise ValueError(f"{option} already exists in node.")
        self.set_interaction(command, action)
    
    # Parse an option string and return the Node that it matches!
    def parse(self, command, args, kwargs) -> "Node":
        if command in self.__options:
            return self.__options[command].perform(self, args, kwargs)
        # Return a None-type object if the option doesn't exist.
        return None

    def copy(self) -> "Node":
        return Node(self.description, self.options)

    def describe(self):
        print(self.description)
    
    def has_interaction(self, command):
        return (command in self.__options)
    
    def set_connection(self, direction, node):
        if direction in self.__connections:
            self.__connections[direction] = node
        else:
            raise ValueError(f"Invalid direction: \"{direction}\"")
    
    def add_connection(self, direction, node):
        if direction in self.__connections:
            if not self.__connections[direction] is None:
                raise ValueError(f"Node already has a connection to the \"{direction}\"")
            opposite_direction = None
            if direction == "north":
                opposite_direction = "south"
            elif direction == "east":
                opposite_direction = "west"
            elif direction == "south":
                opposite_direction = "north"
            elif direction == "west":
                opposite_direction = "east"
            self.set_connection(direction, node)
            node.set_connection(opposite_direction, self)
        else:
            raise ValueError(f"Invalid direction: \"{direction}\"")

    
    def get_connection(self, direction):
        if direction in self.__connections:
            return self.__connections[direction]
        else:
            raise ValueError(f"Invalid direction: \"{direction}\"")
