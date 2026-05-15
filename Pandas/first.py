import pandas as pd


# a = [1,2,3,4]



# zero = pd.Series(a, index = ["x","y","z","w"])
# print(zero)
# print("Finding out the value:", zero["x"])

# df = pd.read_csv(r"C:\Users\NIELIT\Downloads\data.csv")
# print(df.to_string())


# # Give me a machine learning model to predict the price of a house based on its size and location.
# import LinearRegression
# import numpy as np

# # Sample data: size (in square feet) and price (in dollars)
# data = {
#     'size': [1500, 2000, 2500, 3000, 3500],
#     'price': [300000, 400000, 500000, 600000, 700000]
# }
# # Create a DataFrame
# df = pd.DataFrame(data)

# # Prepare the data
# X = df[['size']]  # Features (size)
# y = df['price']  # Target variable (price)
# # Create and fit the model
# model = LinearRegression()
# model.fit(X, y)

# # Predict the price of a house with a size of 2750 square feet
# predicted_price = model.predict([[2750]])
# print(f"The predicted price of a house with a size of 2750 square feet is: ${predicted_price[0]:.2f}")


# lr = pd.read_csv(r"C:\\Users\\NIELIT\\Downloads\\data.csv")
# print(lr)


# pd.options.display.max_rows = 80

# lr = pd.read_csv(r"C:\Users\NIELIT\Downloads\data.csv")                       
# print(lr)


# print(lr.head(80).to_string())

# print(lr.tail(80).to_string())

# df = pd.read_json('https://www.w3schools.com/python/pandas/data.js')
# print(df.to_string())



