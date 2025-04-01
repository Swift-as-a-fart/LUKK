from command import Command
import sys

jump_command = Command(lambda _, __, ___: print("You jump up and down. Fun!"))
look_command = Command(lambda node, _, __: node.describe())
quit_command = Command(lambda _, __, ___: sys.exit())
# concept # see_password_command = (lambda _, __, ___: recieve_password print(f"Password: {password}"))
yell_command = Command(lambda _, __, ___: print("Aaaarrrrgggghhhh!"))
openmailbox_command = Command(lambda node, _, __: print("opening the mailbox reveals a key."))
credits_command = Command(lambda _, __, ___: print("Credits:  \t \t \t \t \t \t \t \t \t \t \t \t \t  Lead programmer: Noah Keyes   \t \t \t \t \t \t \t \t \t \t \t  Associate programmer: William Ciesialka \t \t \t \t \t \t \t \t \t \t A game inspired by: Zork, Made by MIT"))
def go_func(node, args, kwargs):
    if args is None:
        raise TypeError("direction must be type str, not NoneType")
    elif len(args) < 1:
        raise ValueError("No direction included")
    else:
        direction = args[0]
        new_node = node.get_connection(direction)
        if new_node is None:
            print(f"Cannot go \"{direction}.\"")
            return node
        else:
            return new_node
go_command = Command(go_func)
