
def int_check(question, low, high):
    """Checks users enter an integer"""

    error = f"please enter between {low} or {high}."

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            if response >= low and response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


# Main program

# Ask for their age and check it's between 1 and 10
items = int_check("Enter the number of items between 1 and 10 ", 1, 10)
print(f"You've selected {items} items")

# Ask for their age and check it's between 5 and 20
items_2 = int_check("Enter the number of items between 5 and 20 ", 5, 20)
print(f"You've selected {items_2} items")