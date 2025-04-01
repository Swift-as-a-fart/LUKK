#imports 
import sys 
import pickle
from gamemap import build_map 
from parser import CommandParser
from command import Command
from commands import *
# from passwords import Password
# Zork startup
print(":::      :::    ::: :::    ::: :::    :::")
print(":+:      :+:    :+: :+:   :+:  :+:   :+: ")         
print("+:+      +:+    +:+ +:+  +:+   +:+  +:+  ")
print("+#+      +#+    +#+ +#++:++    +#++:++   ")
print("+#+      +#+    +#+ +#+  +#+   +#+  +#+  ")
print("#+#      #+#    #+# #+#   #+#  #+#   #+# ")
print("######### ########  ###    ### ###    ###")
print("                                         ")
print("                                         ")
print("                [1] Play                 ")
print("                [2] Exit                 ")
print("   [3] Import save data (via password)   ")
print("    ^          unfinished                ")
print("              [4]  Credits               ")
print("")
print("")
ans = int(input("> "))
#Zork code
if ans == 4:
    print("Credits:")
    print("Lead programmer: Noah Keyes")
    print("Associate programmer: William Ciesialka")
    print("A game inspired by: Zork, Made by MIT")
    sys.exit
#if ans == 3:
#    password = str(input("insert password : "))
#    load_password
if ans == 2:
    print("Goodbye!")
    sys.exit
if ans == 1: 
    # Map-building @ gamemap.py
    start_node = build_map()
    previous_node = None
    current_node = start_node
    player_alive = True
    print(current_node.description)
    # Create command parser
    command_parser = CommandParser()
    # Create action parsers
    command_parser.add_command("jump", jump_command)
    command_parser.add_command("look", look_command)
    command_parser.add_command("quit", quit_command)
    command_parser.add_command("go", go_command)
    command_parser.add_command("yell", yell_command)
    #command_parser.add_command("open_mailbox", openmailbox_command, mailbox = True)
    command_parser.add_command("credits", credits_command)

    while player_alive:
        print()
        print()
        decision = input(">")
        new_node = command_parser.parse_string(current_node, decision)
        if new_node:
            previous_node = current_node
            current_node = new_node
            print(current_node.description)
        else:
            continue
    if not ans == 1 or not ans == 2:
        print("invalid answer")
