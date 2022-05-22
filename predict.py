#############
# Libraries #
#############

import numpy as np
import sys

#############
# Functions #
#############

def get_thetas():
    """
    Reads the thetas stored in .thetas.
    If .thetas doesn't exist, thetas will be set to (0, 0).
    """
    try:
        with open(".thetas", "r") as f:
            thetas = f.read().split()
            thetas = np.array([[float(thetas[0])], [float(thetas[1])]])
    except:
        print("\033[93mCaution! .thetas file is not present or is corrupted. thetas will be set to (0, 0)\033[0m")
        thetas = np.array([[0.0], [0.0]])
    return thetas

def show_welcome_banner():
    """
    Displays a welcome banner.
    """
    print("\033[1m")
    print(" ____  ____  ____  ____  ____  ___  ____     ____  _   _  ____     _  _  ____  _  _  ____ ") 
    print("(  _ \(  _ \( ___)(  _ \(_  _)/ __)(_  _)___(_  _)( )_( )( ___)___( \( )( ___)( \/ )(_  _)")
    print(" )___/ )   / )__)  )(_) )_)(_( (__   )( (___) )(   ) _ (  )__)(___))  (  )__)  )  (   )(  ")
    print("(__)  (_)\_)(____)(____/(____)\___) (__)     (__) (_) (_)(____)   (_)\_)(____)(_/\_) (__) ")
    print()
    print("\033[0m")
    return

def show_goodbye_banner():
    """
    Displays a goodbye banner.
    """
    print("\033[1m")
    print()
    print("We hope you have found PREDICT-THE-NEXT useful.")
    print("If you have any issues, feel free to contact us at: https://github.com/pgomez-a")
    print()
    print("BYE! :)")
    print("\033[0m")
    return

###########
# Program #
###########

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("\033[91mError. This executable takes no arguments.\033[0m")
        print()
        sys.exit(1)
    thetas = get_thetas()
    try:
        show_welcome_banner()
        while True:
            mileage = input("\033[1mPlease, enter the mileage of the car to predict its price:\n>> \033[0m")
            try:
                mileage = float(mileage)
                if mileage < 0:
                    print("\033[91mError. Cars can't have a negative mileage.\033[0m")
                    print()
                else:
                    price = thetas[0] + thetas[1] * mileage
                    print("The estimated price for a mileage of {}km is: {:.4f}$".format(mileage, price[0]))
                    print()
            except:
                print("\033[91mError. The given input is not a valid mileage. Mileage should be numeric.\033[0m")
                print()
    except:
        show_goodbye_banner()
