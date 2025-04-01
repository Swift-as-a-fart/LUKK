# Command parser
from command import Command
from node import Node

class CommandParser:

    def __init__(self):
        # Create list of commands
        self.__commands = {}
    
    def add_command(self, command, action):
        if command in self.__commands:
            raise ValueError(f"Command \"{command}\" already exists!")
        self.set_command(command, action)
    
    def set_command(self, command, action):
        self.__commands[command] = action

    def parse(self, node, cmd, args=None, kwargs=None):
        if cmd in self.__commands:
            # If the node has a special interaction, let the node take over
            if node.has_interaction(cmd):
                return node.parse(cmd, args, kwargs)
            else:
                # Run the default action
                return self.__commands[cmd].perform(node, args, kwargs)
        else:
            print(f"I don't know how to \"{command}\"")
            return None
    
    def parse_string(self, node, string):
        split = string.lower().split()
        if len(split) > 1:
            return self.parse(node, split[0], split[1:])
        else:
            return self.parse(node, string.lower(), None) 
