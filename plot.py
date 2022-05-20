import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    try:
        dataset = pd.read_csv("data.csv")
        X = dataset.iloc[:, 0]
        Y = dataset.iloc[:, 1]
        plt.scatter(X, Y, alpha = 0.5)
        plt.show()
    except:
        print("Caution! data.csv is not present or is corrupted.")
