#############
# Libraries #
#############

import matplotlib.pyplot as plt
import pandas as pd
import sys

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
    return X_norm, Y_norm

def progress_bar(iters):
    """
    Shows a progress bar to see the evolution of the model.
    """
    bar = ""
    for it in range(iters):
        perc = (100 * it) / iters
        if perc % 2 == 0:
            bar += "="
        print("\033[1m[{: <51}] {}/{}  {:.0f}%\033[0m".format(bar + ">", it + 1, iters, perc), end = "\r")
        yield it
    print()

def gradient_descent(X, Y, verbose):
    """
    Computes the gradient descent of the given parameters.
    """
    print("\033[1mTraining algorithm...\033[0m")
    X_norm, Y_norm = normalize_values(X, Y)
    theta0 = 0.0
    theta1 = 0.0
    alpha = 0.01
    iters = 10000
    plt.ion()
    for it in progress_bar(iters):
        Y_norm_hat = theta0 + theta1 * X_norm
        if verbose and it % 50 == 0:
            Y_hat = Y_norm_hat * (max(Y) - min(Y)) + Y.mean()
            plt.title("Car Price Prediction Model  {}/{}".format(it + 1, iters) )
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
    Y_hat = Y_norm_hat * (max(Y) - min(Y)) + Y.mean()
    theta1 = (Y_hat[1] - Y_hat[0]) / (X[1] - X[0])
    theta0 = Y_hat[0] - theta1 * X[0]
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
        X = dataset.iloc[:, 0]
        Y = dataset.iloc[:, 1]
        theta0, theta1 = gradient_descent(X, Y, verbose)
        print("\033[1mStoring values...\033[0m")
        with open(".thetas", "w") as f:
            f.write(str(theta0) + "\n" + str(theta1))
        print()
    except:
        print("\033[93mCaution! data.csv is not present or is corrupted.\033[0m")
        print()
        sys.exit(1)
