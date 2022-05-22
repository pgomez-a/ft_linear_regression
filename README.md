# ft_linear_regression

Welcome to the amazing world of Machine Learning! This time we are going to implement a linear regression algorithm to predict the price of a car for a given mileage. For this, the dataset that we will use will be data.csv. For today's project, we will need to read this dataset and perform a linear regression with a gradient descent algorithm, finding the best regression line that fits the dataset.<br>

Different executables have been implemented to perform different tasks. Instructions for using each executable are shown below. Feel free to play with them however you want. And of course feel free to contact me if you have any problems playing with it.

- **predict.py:** predicts the price of a car for a given mileage.
  - It takes no arguments.
  - The requested mileage must be float.
  - Press ^D to stop execution.
  - Gets theta0 and theta1 stored in .thetas.
  - If .thetas doesn't exist, theta0 and theta1 are set to 0.0.

<img width="500" alt="predict" src="https://user-images.githubusercontent.com/74931024/169715529-8395709a-2d1a-4168-b494-c3fd31c4456f.png">

### What is linear regression?
**Linear regression** is a statistical model that allows us to predict the value of one variable from the values of other variables. This will be possible only if there is a **dependency between these variables.** With this project we are trying to predict the price of a car given its mileage. Since the mileage of a car affects its price, we will try to find a pattern between the price and the mileage of a car. Once the pattern is found, we will be able to make such predictions.<br>

<div align="center">
<img width=400 alt="linear_regression" src="https://user-images.githubusercontent.com/74931024/169714421-206a152d-1683-4d51-9628-49186b323ac9.png">
<img width=400 alt="linear_regression" src="https://user-images.githubusercontent.com/74931024/169714395-3a0a370a-8073-4bb3-9485-02a87abdafd8.png">
</div>
                                                                                                                                                    
**Disclaimer:** what we are doing here is a **simple linear regression.** Real world applications involve the use of many variables to predict another. This is called **multiple linear regression.** For example, there are many factors that affect the price of a car. We cannot predict its price just by knowing its mileage. But to implement multiple regression models, we first need to fully understand how simple linear regression works. This is the real goal of the project: to be able to understand how to train a machine learning model using simple linear regression.<br>

<div align="center">
<img width=350 alt="Precit-Evaluate-Improve" src="https://user-images.githubusercontent.com/74931024/169713947-5da770bd-ed9d-4a7c-8875-81806f2b605a.jpeg">
</div>
