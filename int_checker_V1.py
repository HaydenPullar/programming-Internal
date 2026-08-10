# functions go here
def int_check(question):

    """Checks users enter an integer"""

    error = "Oops - please enter 1 or above."

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            if response >= 1 :

                return response


            else:
                print(error)

        except ValueError:
                print(error)


# Main program

# Ask for their age and check it's between 12 and 120

items = int_check("Enter the number of items. Must be at least 1: ")

print(f"You selected {items} items")