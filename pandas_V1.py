
import pandas
import numpy as np

# variables

drinks = ["Coffee", "Can V", "Milkshake"]
drink_prices = [6, 4, 7]

drinks_menu = {
    'Drinks': drinks,
    'Prices': drink_prices
}

# Main program
# Rearranging index-
d_menu = pandas.DataFrame(drinks_menu)
# Rearranging index
d_menu.index = np.arange(1, len(d_menu) + 1)
print(d_menu)





