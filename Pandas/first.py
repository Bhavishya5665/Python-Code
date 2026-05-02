import pandas as pd


# a = [1,2,3,4]



# zero = pd.Series(a, index = ["x","y","z","w"])
# print(zero)
# print("Finding out the value:", zero["x"])

df = pd.read_csv(r"C:\Users\NIELIT\Downloads\data.csv")
print(df.to_string())
