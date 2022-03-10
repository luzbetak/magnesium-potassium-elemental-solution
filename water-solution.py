#!/usr/bin/env python3 
import os
os.system('clear')
#---------------------------------------------------------------------------------#
liter  = 1000     # in ml
tsp    = 4.92892
tbl    = 14.7868

#---------------------------------------------------------------------------------#
def magnesium():

    amount  = 30   # Powder amount in grams
    MgCl2   = 25.5 # Magnesium Chlorid contains 25.5% by mass 
    content = round((amount / 100) * MgCl2, 3)


    print("*" * 50)
    print("* Distilled Water Solution = {:.2f} ml".format(liter))
    print("* Magnesium Chloride {}g   = Magnesium {:.2f}g".format(amount, content))
    print("*" * 50)


    teaspoon   = ((content / liter) * tsp) * 1000
    tablespoon = ((content / liter) * tbl) * 1000

    print("-" * 50)
    print("1.0 Teaspoon   = {:5.1f} mg".format(teaspoon))
    print("0.5 Tablespoon = {:5.1f} mg".format(tablespoon/2))
    print("1.0 Tablespoon = {:5.1f} mg".format(tablespoon))
    print("-" * 50)
    print("Daily Requirements: 420 mg = {:3.1f} Tablespoons".format(420/tablespoon))
    print("-" * 50)



#---------------------------------------------------------------------------------#
def potassium():

    amount  = 30    # Powder amount in grams
    KCl     = 52.45 # Potassium Chloride contains 52.45% by mass 
    content = (amount / 100) * KCl
    print("*" * 50)
    print("* Distilled Water Solution = {:.2f} ml".format(liter))
    print("* Potassium Chloride {}g   = Potassium {:.2f}g".format(amount, content))
    print("*" * 50)


    teaspoon   = ((content / liter) * tsp) * 1000
    tablespoon = ((content / liter) * tbl) * 1000


    print("-" * 50)
    print("1.0 Teaspoon   = {:5.1f} mg".format(teaspoon))
    print("0.5 Tablespoon = {:5.1f} mg".format(tablespoon/2))
    print("1.0 Tablespoon = {:5.1f} mg".format(tablespoon))
    print("-" * 50)
    print("Daily Requirements: 4700mg = {:3.1f} Tablespoons".format(4700/tablespoon))
    print("-" * 50)


#---------------------------------------------------------------------------------#
def main():

    magnesium()
    print("\n")
    potassium()


#---------------------------------------------------------------------------------#
if __name__ == "__main__":

    main()

