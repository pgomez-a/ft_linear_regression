# ft_linear_regression

<img width="1098" alt="ft_linear_regression" src="https://user-images.githubusercontent.com/74931024/169718424-69861d78-9cde-4c56-9cf5-9ee6171f8f1c.png">


**If you want to learn more about IT topics, [I invite you to join my Patreon channel](https://www.patreon.com/pgomeza) and visit my website:** [**IA Notes**](https://ia-notes.com/)

Welcome to the amazing world of **Machine Learning!** This time we are going to implement a linear regression algorithm to predict the price of a car for a given mileage. For this, the dataset that we will use will be data.csv. For today's project, we will need to read this dataset and perform a linear regression with a gradient descent algorithm, finding the best regression line that fits the dataset.<br>

Different executables have been implemented to perform different tasks. Instructions for using each executable are shown below. Feel free to play with them however you want. And of course feel free to contact me if you have any problems playing with it.

- **predict.py:** predicts the price of a car for a given mileage.
  - Takes no arguments.
  - The requested mileage must be float.
  - Press **^D** to stop execution.
  - Gets theta0 & theta1 stored in .thetas to make the prediction.
  - If .thetas doesn't exist, theta0 & theta1 are set to 0.0.

- **train.py:** trains the model using normalization and gradient descent.
  - Takes the argument **-v** to plot model training.
  - Shows a progress bar while training the model.
  - Calculates theta0 & theta1 for future predictions.
  - theta0 & theta1 are stored in .thetas
  - Reads data.csv dataset by default.

<div align="center">
<img width=500 alt="train.py -v" src="https://user-images.githubusercontent.com/74931024/169717621-de37be6f-f92a-48ca-94d8-d4fb49c24a3f.gif">
</div>

- **cost.py:** displays the current cost for the model.
  - Takes the argument **-v** to plot 3D graph related to theta0 & theta1.
  - Takes the argument **-v0** to plot 2D graph related to theta0.
  - Takes the argument **-v1** to plot 2D graph related to theta1.
  - Takes theta0 & theta1 stored in .thetas to compute the cost.
  - If .thetas doesn't exist, theta0 & theta1 are set to 0.0.
  
<div align="center">
<img width="400" alt="theta0 cost" src="https://user-images.githubusercontent.com/74931024/169717912-372db0da-2184-4810-93e1-a5d5759b76e1.png">
<img width="400" alt="theta1 cost" src="https://user-images.githubusercontent.com/74931024/169717937-76a81cdb-c9f5-4291-a426-28b5bb479e40.png">
<img width="400" alt="3d_cost_1" src="https://user-images.githubusercontent.com/74931024/169717020-cda7e33d-bb8e-461b-b53e-f8ff23edffd4.png">
<img width="400" alt="3d_cost_2" src="https://user-images.githubusercontent.com/74931024/169716937-4d429566-612f-4f2e-93c8-db7c850a727f.png">
</div>

- **plot.py:** plots the model with the regression line.
  - Takes two float values as arguments to plot a point.
  - Takes theta0 & theta1 stored in .thetas to plot the regression line.
  - If .thetas doesn't exist, theta0 & theta1 are set to 0.0.

<div align="center">
<img width=400 alt="linear_regression" src="https://user-images.githubusercontent.com/74931024/169714421-206a152d-1683-4d51-9628-49186b323ac9.png">
<img width=400 alt="linear_regression" src="https://user-images.githubusercontent.com/74931024/169714395-3a0a370a-8073-4bb3-9485-02a87abdafd8.png">
</div>
  
### What is linear regression?
**Linear regression** is a statistical model that allows us to predict the value of one variable from the values of other variables. This will be possible only if there is a **dependency between these variables.** With this project we are trying to predict the price of a car given its mileage. Since the mileage of a car affects its price, we will try to find a pattern between the price and the mileage of a car. Once the pattern is found, we will be able to make such predictions.<br>
                                                                                                                                                    
**Disclaimer:** what we are doing here is a **simple linear regression.** Real world applications involve the use of many variables to predict another. This is called **multiple linear regression.** For example, there are many factors that affect the price of a car. We cannot predict its price just by knowing its mileage. But to implement multiple regression models, we first need to fully understand how simple linear regression works. This is the real goal of the project: to be able to understand how to train a machine learning model using simple linear regression.<br>

<div align="center">
<img width=350 alt="Precit-Evaluate-Improve" src="https://user-images.githubusercontent.com/74931024/169713947-5da770bd-ed9d-4a7c-8875-81806f2b605a.jpeg">
</div>
