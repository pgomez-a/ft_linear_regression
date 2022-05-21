#############
# Libraries #
#############

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

def gradient_descent(X, Y):
    """
    Computes the gradient descent of the given parameters.
    """
    print("\033[1mTraining algorithm...\033[0m")
    theta0 = 0.0
    theta1 = 0.0
    alpha = 0.01
    iters = 10000
    for iter in range(iters):
        Y_hat = estimate_price(theta0, theta1, X)
        tmpTheta0 = sum(Y_hat - Y) / Y.size
        tmpTheta1 = sum((Y_hat - Y) * X) / Y.size
        theta0 -= alpha * tmpTheta0
        theta1 -= alpha * tmpTheta1
    return theta0, theta1

###########
# Program #
###########

if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("\033[91mError. This executable takes no arguments.\033[0m")
        print()
        sys.exit(1)
    try:
        print("\033[1mReading dataset...\033[0m")
        dataset = pd.read_csv("data.csv")
        time.sleep(1)
        X = dataset.iloc[:, 0]
        Y = dataset.iloc[:, 1]
        X_norm, Y_norm = normalize_values(X, Y)
        theta0, theta1 = gradient_descent(X_norm, Y_norm)
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
