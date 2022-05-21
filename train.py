#############
# Libraries #
#############

import matplotlib.pyplot as plt
import pandas as pd
import time
import sys

from predict import estimate_price

#############
# Functions #
#############

def normalize_values(X, Y):
    """
    Normalizes X and Y pandas.dataframes to improve linear regression performance.
    """
    print("\033[1mNormalizing values...\033[0m")
    X_norm = (X - X.mean()) / (max(X) - min(X))
    Y_norm = (Y - Y.mean()) / (max(Y) - min(Y))
    time.sleep(1)
    return X_norm, Y_norm

def progress_bar(iters):
    """
    Shows a progress bar to see the evolution of the model.
    """
    bar = ""
    for i in range(iters):
        pos = (100 * i) / iters
        if pos % 2 == 0:
            bar += "="
        print("\033[1m[{: <51}] {}/{}  {:.0f}%\033[0m".format(bar + ">", i + 1, iters, pos), end = "\r")
        yield i
    print()

def gradient_descent(X_norm, Y_norm, X, Y, verbose):
    """
    Computes the gradient descent of the given parameters.
    """
    print("\033[1mTraining algorithm...\033[0m")
    theta0 = 0.0
    theta1 = 0.0
    alpha = 0.01
    iters = 10000
    plt.ion()
    for iter in progress_bar(iters):
        Y_norm_hat = estimate_price(theta0, theta1, X_norm)
        Y_hat = Y_norm_hat * (max(Y) - min(Y)) + Y.mean()
        if verbose and iter % 50 == 0:
            plt.title("Car Price Prediction Model")
            plt.ylabel("Prices")
            plt.xlabel("Mileages")
            plt.scatter(X, Y, alpha = 0.5)
            plt.plot(X, Y_hat, color = "red")
            plt.draw()
            plt.pause(0.000000001)
            plt.clf()
        tmpTheta0 = sum(Y_norm_hat - Y_norm) / Y_norm.size
        tmpTheta1 = sum((Y_norm_hat - Y_norm) * X_norm) / Y_norm.size
        theta0 -= alpha * tmpTheta0
        theta1 -= alpha * tmpTheta1
    return theta0, theta1

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
        print("\033[1mReading dataset...\033[0m")
        dataset = pd.read_csv("data.csv")
        time.sleep(1)
        X = dataset.iloc[:, 0]
        Y = dataset.iloc[:, 1]
        X_norm, Y_norm = normalize_values(X, Y)
        theta0, theta1 = gradient_descent(X_norm, Y_norm, X, Y, verbose)
        print("\033[1mStoring values...\033[0m")
        with open(".thetas", "w") as f:
            f.write(str(theta0) + " " + str(theta1) + "\n")
            f.write(str(X.mean()) + " " + str(max(X)) + " " + str(min(X)) + "\n")
            f.write(str(Y.mean()) + " " + str(max(Y)) + " " + str(min(Y)) + "\n")
        time.sleep(1)
        print()
    except:
        print("\033[93mCaution! data.csv is not present or is corrupted.\033[0m")
        print()
        sys.exit(1)
