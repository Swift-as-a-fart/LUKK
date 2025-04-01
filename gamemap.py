from node import Node
from os import linesep
import sys
# Our map-building function.
# Returns the starting node.
def build_map() -> Node:
    start_screen = []
    start_screen += ("You are standing in an open field west of a white house, with a boarded front")
    start_screen += (" door. There is a small mailbox here.")
    start_text = linesep.join(start_screen)
    start_node = Node(start_text)
    white_house_node = Node("You approach the white house. The door inside is boarded shut.")
    start_node.add_connection("west", white_house_node)

    return start_node
