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

def show_cost_function(theta0, theta1):
    """
    Displays cost function.
    """
    thetas = [list(), list()]
    error = [list(), list()]
    Y_hat = [0.0, 0.0]
    count = -2.0
    while count < 2.0:
        Y_hat[0] = (count + theta1 * X_norm) * (max(Y) - min(Y)) + Y.mean()
        Y_hat[1] = (theta0 + count * X_norm) * (max(Y) - min(Y)) + Y.mean()
        cost0 = np.sum((Y_hat[0] - Y)**2) / (2 * Y.size)
        cost1 = np.sum((Y_hat[1] - Y)**2) / (2 * Y.size)
        thetas[0].append(count)
        thetas[1].append(count)
        error[0].append(cost0)
        error[1].append(cost1)
        count += 0.01
    plt.plot(thetas[0], error[0], color = "blue", label = "theta0")
    plt.plot(thetas[1], error[1], color = "orange", label = "theta1")
    plt.legend()
    plt.show()
    return

###########
# Program #
###########

if __name__ == '__main__':
    verbose = 0
    if len(sys.argv) == 2 and sys.argv[1] == "-v":
        verbose = 1
    elif len(sys.argv) != 1:
        print("\033[91mError. This executable takes the argument -v.\033[0m")
        print()
        sys.exit(1)
    try:
        dataset = pd.read_csv("data.csv")
        X = dataset.iloc[:, 0]
        Y = dataset.iloc[:, 1]
        X_norm = (X - X.mean()) / (max(X) - min(X))
        Y_norm = (Y - Y.mean()) / (max(Y) - min(Y))
    except:
        print("\033[93mCaution! data.csv is not present or is corrupted.\033[0m")
        print()
        sys.exit(1)
    try:
        with open(".thetas", "r") as f:
            thetas = f.read()
            thetas = thetas.split()
            thetas = np.array([float(thetas[0]), float(thetas[1])]).reshape(-1, 1)
    except:
        print("\033[93mCaution! .thetas is not present or is corrupted.\033[0m")
        thetas = np.array([0.0, 0.0]).reshape(-1, 1)
    Y_hat = thetas[0] + thetas[1] * X_norm
    Y_hat = Y_hat * (max(Y) - min(Y)) + Y.mean()
    cost = np.sum((Y_hat - Y)**2) / (2 * Y.size)
    plt.scatter(thetas[0], cost, color = "blue")
    plt.scatter(thetas[1], cost, color = "orange")
    print("The cost of the model with")
    print("thetas: \033[1m({}, {})\33[0m".format(thetas[0][0], thetas[1][0]))
    print("is:     \033[1m{:.4f}\033[0m".format(cost))
    print()
    if verbose == 1:
        show_cost_function(thetas[0], thetas[1])
