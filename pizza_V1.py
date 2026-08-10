
import pandas
import numpy as np

 # Functions go here
def make_statement(statement, decoration):
     """Emphasizes heading by adding decoration
     at the start and end"""

     print(f"{decoration * 3}: {statement} {decoration * 3} ")

def string_check(question, valid_answers=('yes', 'no'),
                 num_letters=1):
    """Checks that users enter the full word
    or the 'n' letter/s of a word from a range of valid responses"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the 'n' letters
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")

def instructions():


    print('''

    1. The pizza menu will be displayed with the pizza names, prices, and menu numbers.
    2. Enter how many pizzas you would like to order (between 1 and 5).
    3. Select each pizza by entering its menu number.
    4. After choosing your pizzas, you will be asked if you would like any extras.
    - Enter yes (y) or no (n). 
    5. If you choose extras:
    - The extras menu will be displayed.
    - Enter how many extras you would like.
    - Select each extra by entering its menu number.
    6. Once all selections have been made, the program will display:
    - A list of all pizzas and extras you selected.
    - The price of each item.
    - The total cost of your order.
    7. Choose a payment method by entering:
    - ca for cash, or
    - cr for credit.
    8. Finally program will confirm your payment method.


    ''')

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

# Variables

number_of_pizzas = 0
number_of_extras = 0
user_selection = []
user_selection_prices = []
all_user_selections = {
    'selections': user_selection,
    'Prices':user_selection_prices
}

pizza = ["Pepperoni", "Hawaiian", "Meat Lovers",]
pizza_prices = [13, 12, 15,]

pizza_menu = {
    'Pizza': pizza,
    'Prices': pizza_prices
}

extras = ["Fries", "Salad", "Garlic Bread", "Lemonade", "Fanta", "Cola"]
extras_prices = [5, 7, 15, 4, 3, 5]

extras_menu = {
    'extras': extras,
    'Prices':extras_prices
}

payment = ["cash", "credit"]

# Main program

make_statement("welcome to C.H.U.D. pizzas", "🍕")

print()
want_instructions = string_check("would you like to know how to order your food? ")

if want_instructions == "yes":
    instructions()


# Rearranging index-
p_menu = pandas.DataFrame(pizza_menu)
# Rearranging index
p_menu.index = np.arange(1, len(p_menu) + 1)
print(p_menu)

# Rearranging index-
e_menu = pandas.DataFrame(extras_menu)
# Rearranging index
e_menu.index = np.arange(1, len(e_menu) + 1)



# Ask the user how many pizzas would they like
pizzas = int_check("How many pizzas would you like? ", 1, 5)
print(f"You've selected {pizzas} pizzas")

while number_of_pizzas < pizzas:

    items = int_check(f'what would you like?', 1, 3)

    if items == 1:
        selected_pizza = pizza[items - 1]
    elif items == 2:
        selected_pizza = pizza[items - 1]
    else:
        selected_pizza = pizza[items - 1]

    print(f"You chose {selected_pizza} ${pizza_prices[items - 1]}")
    number_of_pizzas += 1
    # append pizzas and prices into user selection list
    user_selection.append(selected_pizza)
    user_selection_prices.append(pizza_prices[items - 1])

# Ask if the user wants any extras
display_extras = string_check("Would you like any extras? ")

if display_extras == "yes":
    print(e_menu)

    extra_item = int_check("How many extras would you like? ", 1, 6)
    print(f"You've selected {extra_item} extras")

    while number_of_extras < extra_item:

        extra_selection = int_check(f'what would you like? ', 1, 6)

        if  extra_selection == 1:
            selected_extras = extras[extra_selection - 1]
        elif  extra_selection == 2:
            selected_extras = extras[extra_selection - 1]
        elif  extra_selection == 3:
            selected_extras = extras[extra_selection - 1]
        elif  extra_selection == 4:
            selected_extras = extras[extra_selection - 1]
        elif  extra_selection == 5:
            selected_extras = extras[extra_selection - 1]
        else :
            selected_extras = extras[extra_selection - 1]

        print(f"You chose {selected_extras} ${extras_prices[extra_selection - 1]}")
        number_of_extras += 1
        # append pizzas and prices into user selection list
        user_selection.append(selected_extras)
        user_selection_prices.append(extras_prices[extra_selection - 1])

# Rearranging index - user selections
final_user_selection = pandas.DataFrame(all_user_selections)
# Rearranging index
final_user_selection.index = np.arange(1, len(final_user_selection) + 1)

print(final_user_selection)
print(f"Total: ${sum(user_selection_prices)}")

pay_method = string_check("Choose a payment method cash(ca) or credit(cr): ", payment, 2 )
if pay_method == "cash":
    print(f"You chose to pay by cash")
else:
    print(f"You chose {pay_method}")

print()
print("program has ended")
