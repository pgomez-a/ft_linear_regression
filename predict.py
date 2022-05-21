#############
# Libraries #
#############

import numpy as np
import sys

#############
# Functions #
#############

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
    print("\n\n")
    print("We hope you have found PREDICT-THE-NEXT useful.")
    print("If you have any issues, feel free to contact us at: https://github.com/pgomez-a")
    print()
    print("BYE! :)")
    print("\033[0m")
    return

def estimate_price(theta0, theta1, mileage):
    """
    Predicts the price of a car for a given mileage.
    """
    return theta0 + theta1 * mileage

###########
# Program #
###########

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("\033[91mError. This executable takes no arguments.\033[0m")
        print()
        sys.exit(1)
    try:
        with open(".thetas", "r") as f:
            init_values = f.read()
            init_values = init_values.split()
            thetas = np.array([float(init_values[0]), float(init_values[1])]).reshape(-1, 1)
            mileage_mean = float(init_values[2])
            mileage_max = float(init_values[3])
            mileage_min = float(init_values[4])
            price_mean = float(init_values[5])
            price_max = float(init_values[6])
            price_min = float(init_values[7])
    except Exception as f:
        thetas = np.array([0.0, 0.0]).reshape(-1, 1)
    try:
        show_welcome_banner()
        while True:
            mileage = input("\033[1mPlease, enter the mileage of the car to predict its price:\n>> \033[0m")
            try:
                mileage = float(mileage)
                if mileage < 0:
                    print("\033[91mError. Cars can't have a negative mileage.\033[0m")
                    print()
                elif thetas[0] == 0.0 and thetas[1] == 0.0:
                    print("The estimated price for a mileage of {}km is: {:.4f}$".format(mileage, 0))
                    print()
                else:
                    mileage_norm = (mileage - mileage_mean) / (mileage_max - mileage_min)
                    price = estimate_price(thetas[0], thetas[1], mileage_norm)[0]
                    price = price * (price_max - price_min) + price_mean
                    print("The estimated price for a mileage of {}km is: {:.4f}$".format(mileage, price))
                    print()
            except:
                print("\033[91mError. The given input is not a valid mileage. Mileage should be numeric.\033[0m")
                print()
    except:
        show_goodbye_banner()
