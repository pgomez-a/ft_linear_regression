#############
# Libraries #
#############

import pandas as pd
import numpy as np

###########
# Program #
###########

if __name__ == '__main__':
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
    print("The cost of the model with")
    print("thetas: \033[1m({}, {})\33[0m".format(thetas[0][0], thetas[1][0]))
    print("is:     \033[1m{:.4f}\033[0m".format(cost))
    print()
