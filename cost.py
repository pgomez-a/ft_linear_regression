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
    verbose = -1
    if len(sys.argv) == 2 and sys.argv[1] == "-v0":
        verbose = 0
    elif len(sys.argv) == 2 and sys.argv[1] == "-v1":
        verbose = 1
    elif len(sys.argv) != 1:
        print("\033[91mError. This executable takes the argument -v[0-1].\033[0m")
        print()
        sys.exit(1)
    return verbose

def read_dataset():
    """
    Reads the dataset and returns its respective values.
    """
    try:
        dataset = pd.read_csv("data.csv")
        X = dataset.iloc[:, 0]
        Y = dataset.iloc[:, 1]
    except:
        print("\033[91mError! data.csv is not present or is corrupted.\033[0m")
        print()
        sys.exit(1)
    return X, Y

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

def show_cost_function(theta0, theta1, X, Y, cost, verbose):
    """
    Displays cost function.
    """
    thetas = [list(), list()]
    error = [list(), list()]
    Y_hat = [0.0, 0.0]
    count = -100.0
    while count < 100.0:
        Y_hat[0] = (theta0 + count) + theta1 * X
        Y_hat[1] = theta0 + (theta1 + count) * X
        cost0 = np.sum((Y_hat[0] - Y)**2) / (2 * Y.size)
        cost1 = np.sum((Y_hat[1] - Y)**2) / (2 * Y.size)
        thetas[0].append(theta0 + count)
        thetas[1].append(theta1 + count)
        error[0].append(cost0)
        error[1].append(cost1)
        count += 0.1
    if verbose == 0:
        plt.plot(thetas[0], error[0], color = "blue", label = "theta0")
        plt.scatter(theta0, cost, color = "blue")
    else:
        plt.plot(thetas[1], error[1], color = "orange", label = "theta1")
        plt.scatter(theta1, cost, color = "orange")
    plt.legend()
    plt.show()
    return

###########
# Program #
###########

if __name__ == '__main__':
    verbose = parse_input(sys.argv)
    X, Y = read_dataset()
    thetas = get_thetas()
    Y_hat = thetas[0] + thetas[1] * X
    cost = sum((Y_hat - Y)**2) / (2 * Y.size)
    print("The cost of the model with")
    print("thetas: \033[1m({}, {})\33[0m".format(thetas[0][0], thetas[1][0]))
    print("is:     \033[1m{:.4f}\033[0m".format(cost))
    print()
    if verbose >= 0:
        show_cost_function(thetas[0], thetas[1], X, Y, cost, verbose)
