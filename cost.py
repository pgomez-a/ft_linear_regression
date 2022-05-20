import pandas as pd
import numpy as np

if __name__ == '__main__':
    try:
        dataset = pd.read_csv("data.csv")
        X = dataset.iloc[:, 0]
        Y = dataset.iloc[:, 1]
        X_norm = (X - X.mean()) / (max(X) - min(X))
        Y_norm = (Y - Y.mean()) / (max(Y) - min(Y))
    except:
        print("Caution! data.csv is not present or is corrupted.")
        sys.exit(1)
    try:
        with open(".thetas", "r") as f:
            init_values = f.read()
            init_values = init_values.split()
            thetas = np.array([float(init_values[0]), float(init_values[1])]).reshape(-1, 1)
    except Exception as f:
        print("Caution! .thetas file is not present or is corrupted.")
        thetas = np.array([0.0, 0.0]).reshape(-1, 1)
    Y_hat = thetas[0] + thetas[1] * X_norm
    Y_hat = Y_hat * (max(Y) - min(Y)) + Y.mean()
    cost = np.sum((Y_hat - Y)**2) / (2 * Y.size)
    print("The cost of the model with thetas ({}, {}) is {}".format(thetas[0][0], thetas[1][0], cost))
