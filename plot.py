#############
# Libraries #
#############

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

#############
# Functions #
#############

def parse_input(argv):
    """
    Parses the input received by the program.
    """
    x_coor = None
    y_coor = None
    if len(argv) == 3:
        try:
            x_coor = float(argv[1])
            y_coor = float(argv[2])
        except:
            print("\033[91mInputError - Points to be plotted must be floating.\033[0m")
            sys.exit(1)
    elif len(argv) != 1:
        print("\033[91mInputError - plot.py can only receive 0 or 2 arguments.\033[0m")
        sys.exit(1)
    return x_coor, y_coor

def init_plot_values():
    """
    Reads the dataset and initializes the values to be plotted.
    """
    try:
        dataset = pd.read_csv("data.csv")
        X = dataset.iloc[:, 0]
        Y = dataset.iloc[:, 1]
        X_norm = (X - X.mean()) / (max(X) - min(X))
        plt.title("Car Price Prediction Model")
        plt.ylabel("Prices")
        plt.xlabel("Mileages")
        plt.scatter(X, Y, alpha = 0.5)
    except:
        print("\033[93mCaution! data.csv is not present or is corrupted.\033[0m")
        sys.exit(1)
    return X, Y, X_norm

def get_thetas():
    """
    Reads the thetas stored in .thetas.
    If .thetas doesn't exist, thetas will be set to (0, 0).
    """
    try:
        with open(".thetas", "r") as f:
            thetas = f.read()
            thetas = thetas.split()
            thetas = np.array([float(thetas[0]), float(thetas[1])]).reshape(-1, 1)
    except:
        print("\033[93mCaution! .thetas file is not present or is corrupted. thetas will be set to (0, 0)\033[0m")
        thetas = np.array([0.0, 0.0]).reshape(-1, 1)
    return thetas

###########
# Program #
###########

if __name__ == '__main__':
    x_coor, y_coor = parse_input(sys.argv)
    X, Y, X_norm = init_plot_values()
    thetas = get_thetas()
    Y_norm_hat = thetas[0] + thetas[1] * X_norm
    Y_hat = Y_norm_hat * (max(Y) - min(Y)) + Y.mean()
    plt.plot(X, Y_hat, color = "red")
    if x_coor != None and y_coor != None:
        plt.scatter(x_coor, y_coor, color = "black")
        plt.plot([x_coor, x_coor], [min(Y), y_coor], color = "orange", linestyle = "dashed")
        plt.plot([min(X), x_coor], [y_coor, y_coor], color = "orange", linestyle = "dashed")
    plt.show()
