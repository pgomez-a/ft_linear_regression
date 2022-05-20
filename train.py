import matplotlib.pyplot as plt
import pandas as pd
import sys

from predict import estimate_price

def normalize_values(X, Y):
    """
    Normalizes X and Y pandas.dataframes to improve linear regression performance.
    """
    X_norm = (X - X.mean()) / (max(X) - min(X))
    Y_norm = (Y - Y.mean()) / (max(Y) - min(Y))
    return X_norm, Y_norm

def gradient_descent(X, Y, theta0, theta1, iters, alpha):
    """
    Computes the gradient descent of the given parameters.
    """
    for iter in range(iters):
        Y_hat = estimate_price(theta0, theta1, X)
        tmpTheta0 = sum(Y_hat - Y) / Y.size
        tmpTheta1 = sum((Y_hat - Y) * X) / Y.size
        theta0 -= alpha * tmpTheta0
        theta1 -= alpha * tmpTheta1
    return theta0, theta1

if __name__ == '__main__':
    try:
        dataset = pd.read_csv("data.csv")
        X = dataset.iloc[:, 0]
        Y = dataset.iloc[:, 1]
        plt.scatter(X, Y, alpha=0.5)
        X_norm, Y_norm = normalize_values(X, Y)
        theta0 = 0.0
        theta1 = 0.0
        iters = 10000
        alpha = 0.01
        theta0, theta1 = gradient_descent(X_norm, Y_norm, theta0, theta1, iters, alpha)
        with open(".thetas", "w") as f:
            f.write(str(theta0) + " " + str(theta1) + "\n")
            f.write(str(X.mean()) + " " + str(max(X)) + " " + str(min(X)) + "\n")
            f.write(str(Y.mean()) + " " + str(max(Y)) + " " + str(min(Y)) + "\n")
    except:
        exc_type, exc_value, exc_tracebakc = sys.exc_info()
        print("Exception: {} - {}".format(exc_type.__name__, exc_value))
        sys.exit(1)
