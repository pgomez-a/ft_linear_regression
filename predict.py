#############
# Libraries #
#############

import numpy as np

#############
# Functions #
#############

def estimate_price(theta0, theta1, mileage):
    """
    Predicts the price of a car for a given mileage.
    """
    return theta0 + theta1 * mileage

###########
# Program #
###########

if __name__ == '__main__':
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
        print("Caution! .thetas file is not present or is corrupted.")
        thetas = np.array([0.0, 0.0]).reshape(-1, 1)
    try:
        while True:
            mileage = input("Please, enter the mileage of the car to predict its price:\n>> ")
            try:
                mileage = float(mileage)
                if mileage < 0:
                    print("Error. Cars can't have a negative mileage.")
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
                print("Error. The given input is not a valid mileage. Mileage should be numeric.")
                print()
    except:
        print("Goodbye! :)")
        print()
