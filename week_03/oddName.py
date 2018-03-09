"""
Kristen Scheuber
Ask the user for their name, error-check to make sure their name is not blank and then print every second
letter of their name.
"""

def main():

    user_name = get_name()
    while user_name == "":
        user_name = get_name()
    print(user_name[::2])


def get_name():
    user_name = input("Your Name: ")
    return user_name


main()