import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys

if __name__ == '__main__':
    try:
        dataset = pd.read_csv("data.csv")
        X = dataset.iloc[:, 0]
        X_norm = (X - X.mean()) / (max(X) - min(X))
        Y = dataset.iloc[:, 1]
        plt.scatter(X, Y, alpha = 0.5)
    except:
        print("Caution! data.csv is not present or is corrupted.")
        sys.exit(1)
    try:
        with open(".thetas", "r") as f:
            init_values = f.read()
            init_values = init_values.split()
            thetas = np.array([float(init_values[0]), float(init_values[1])]).reshape(-1, 1)
    except Exception as f:
        print("Caution! .thetas file is not present or is corrupted. thetas will be set to (0, 0)")
        thetas = np.array([0.0, 0.0]).reshape(-1, 1)
    Y_hat = thetas[0] + thetas[1] * X_norm
    Y_hat = Y_hat * (max(Y) - min(Y)) + Y.mean()
    plt.plot(X, Y_hat, color = "red")
    plt.show()
