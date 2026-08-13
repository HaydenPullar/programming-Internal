
import pandas
import numpy as np


# Functions go here
def not_blank(question):
    """Checks if response is not blank."""

    while True:
        response = input(question)

        if response:
            return response

        print("Sorry, this can't be blank. Please try again.\n")

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
    - ca for cash
    - cr for credit.
    8. program will confirm your payment method.
    9. Choose a delivery method by entering:
    - de for delivery, or pi for pick up.
    10. if you choose delivery:
    - you will enter your name, address, and phone number. 
    - will be a 15 dollar surcharge upon purchase.
    11. if you choose pick up:
    - you will enter your name. 
    12. it will ask you if you want to confirm or cancel your order.
    13. it will ask you if you want to place another order
    - if you choose to place another order the program will repeat from asking how many pizzas you would like.
    - if you don't the pick to place another oder the program will end 
   


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

delivery = ["delivery", "pick up"]

delivery_price = 15

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


# Rearranging index-
e_menu = pandas.DataFrame(extras_menu)
# Rearranging index
e_menu.index = np.arange(1, len(e_menu) + 1)

while True:

    # Ask the user how many pizzas would they like
    print(p_menu)
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


    pay_method = string_check("Choose a payment method cash(ca) or credit(cr): ", payment, 2 )
    if pay_method == "cash":
            print(f"You chose to pay by cash")
    else:
        print(f"You chose {pay_method}")

    # Ask the user if they want delivery or pick up

    delivery_option = string_check("Would you like to delivery(de) or pick up(pi)? ",delivery, 2 )

    if delivery_option == "delivery":
        print("You chose delivery")
        who = not_blank("please enter your name for the order: ")
        address = not_blank("what is your address? ")
        phone_number = int_check("what is your phone number? ", 1, 999999999 )
        print(final_user_selection)
        total_ordering = delivery_price + sum(user_selection_prices)
        print(f"Total: ${total_ordering - delivery_price} \n"             
              f"name: {who} \n"
              f"Address: {address} \n"
              f"Phone number: {phone_number} \n"
              f"Delivery Surcharge: ${delivery_price}\n "
              f"Total: ${total_ordering}")

    else:
        print("You chose pick up")
        who = not_blank("please enter your name for the order: ")
        phone_number = int_check("what is your phone number? ", 1, 999999999 )
        print(final_user_selection)
        print()
        print(f"Total: ${sum(user_selection_prices)}\n "
              f"name: {who}\n"
              f"Phone number: {phone_number}")

# Asks the user if they want to confirm or cancel their order
    confirm = string_check(
    "Would you like to confirm your order?", )
    if confirm == "yes":
        print("Your order has been placed, will be ready in 10 minutes.")
    else:
        print("Your order has not been canceled.")

#Asks the user if they would like to place a new order
    another_order = string_check(
        "Would you like to another order?", )
    if another_order == "yes":
        user_selection.clear()
        user_selection_prices.clear()
        number_of_pizzas = 0
        number_of_extras = 0
        continue
    else:
        break
print()
print("Thank you for your buying at C.H.U.D. pizzas.")
