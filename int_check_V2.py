# Functions go here
def int_check(question):
    """Checks users enter an integer"""

    error = "Oops - please enter an integer."

    while True:

        try:
            # Return the response if it's an integer
            response = int(input(question))

            return response

        except ValueError:
            print(error)


# Main program

while True:
    print()

    # Ask for their age and check it's between 12 and 120
    age = int_check("how old are you?: ")

    # Output error message / success message
    if age <= 18:
        print(f"you are {age} years old, you're a minor")
        continue
    elif age == 50:
        print(f"you are {age} years old, you're half way there")
        continue
    elif age >= 51:
        print(f"you are {age} years old, live your life to the fullest")
    else:
        print(f"you are between 19-49 years old")
        pass

