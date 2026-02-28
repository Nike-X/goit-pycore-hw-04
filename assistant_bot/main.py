# Homework 6, Task 4
# This script implements a helper bot that stores phone contacts. 
# Contacts are stored in a dictionary in the format "name": "phone".
# The bot is launched and prompted via the command line interface.

def parse_input(user_input: str):
    # This function parse user input from CLI

    # Separate user's command (e.g., add contact) and provided arguments (name, phone)
    cmd, *args = user_input.split()

    # Strip unnecessary characters and conver to lowercase to compare 
    # command with predefined
    cmd = cmd.strip().lower()
    return cmd, *args

def check_args(args: list, expected_fields: int):
    # This function checks that user provided enough arguments to command
    # (e.g., to add contact user should provide 2 args - name and phone)
    if len(args) != expected_fields:
        return False
    else:
        return True

def add_contact(args: list, contacts: dict):
    # This function adds new contact to dictionary

    # Check, if user provided both name and phone
    if not check_args(args, expected_fields=2):
        return f"Invalid arguments: {args}."
    
    # Assign name and phone and add to dict new contact
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}."

def change_contact(args: list, contacts: dict):
    # This function changes phone number for existing contact

    # Check, if user provided both name and phone
    if not check_args(args, expected_fields=2):
        return f"Invalid arguments: {args}."
    
    # Check if this name is already listed in dict
    name, phone = args
    if name not in contacts:
        return f"Contact {name} does not exist."
    
    # Assign new phone number to contact
    contacts[name] = phone
    return f"Contact {name} successfully changed. New phone number is {phone}."
    
def show_number(args: list, contacts: dict):
    # This function return phone number of selected contact

    # Check, if user provided contact's name
    if not check_args(args, expected_fields=1):
        return f"Invalid arguments: {args}."
    
    # Assign name from args
    name, = args
    
    # Check if this name is already listed in dict
    if name not in contacts:
        return f"Contact {name} does not exist."
    
    # Return phone number
    return f"User {name} has phone number {contacts[name]}."
    
def all_numbers(contacts: dict):
    # This function returns all contacts in dict, line by line

    # Generate lines for each contact
    lines = [f"User {name} has phone number {phone}." for name, phone in contacts.items()]

    # Join lines to single string and return it (by condition we can print only in main())
    return "\n".join(lines)

def main():
    # Main function, processes user's input, defines commands 
    # and prints responses to console

    # Create empty dict for contacts
    contacts = {}

    # Print greetings
    print("Welcome to the assistant bot!")

    # Wait for user's input
    while True:
        user_input = input("Enter a command: ")

        # Parse user's input to separate command and arguments
        command, *args = parse_input(user_input)

        # Define commands to exit from bot
        if command in ["close", "exit"]:
            print("Good bye!")
            break

        # Just placeholder
        elif command == "hello":
            print("How can I help you?")
        # Add contact to dict, print added contact
        elif command == "add":
            print(add_contact(args, contacts))
        # Change existing contact , print it
        elif command == "change":
            print(change_contact(args, contacts))
        # Show phone number for given name
        elif command == "phone":
            print(show_number(args, contacts))
        # Show all contacts from dict
        elif command == "all":
            print(all_numbers(contacts))
        # Warn about invalid command
        else:
            print("Invalid command.")

# This code executes main() function if script is launched from command line
if __name__ == "__main__":
    main()
