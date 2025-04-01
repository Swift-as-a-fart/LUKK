from node import Node

# Create a Command class for handling our commands
class Command:

    def __init__(self, action=None):
        self.__action = action

    @property
    def action(self):
        return self.__action
    
    def perform(self, node, *args, **kwargs) -> Node:
        # If we have an action, perform it!
        # Pass along any arguments or keyword arguments, too.
        # Return the result of the action!
        if self.action:
            return self.action(node, *args, **kwargs)
