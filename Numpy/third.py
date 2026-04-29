import matplotlib.pyplot as plt


import random

# pyplot is a collection of functions that make matplotlib work like MATLAB. Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, plots some lines in a plotting area, decorates the plot with labels, etc.
#  Create a simple line plot with random data


# x = [1, 2, 3, 4, 5]
# y = [10, 20, 15, 25, 30]
# # plt.plot(x, y)
# plt.show()


# ==============Customising Chart=====================

# plt.figure(figsize=(2,5))
# plt.plot(x,y, color ="red", marker="o", linestyle="dashed", linewidth=2, markersize=8)

# plt.title("The Title is : Dhurandhar Sale 2026")
# plt.xlabel("X-axis label is here")
# plt.ylabel("Y-axis label is here")
# plt.show()



# x =[1,2,3,4,5]
# y1 = [10,20,25,35,45]
# y2 = [20,30,35,45,55]
# plt.plot(x, y1, label = 'Sale 2024')
# plt.plot(x, y2, label = 'Sale 2025')
# plt.title("Dhurandhar Sale Comparision 2024 & 2025")
# plt.xlabel("Months")
# plt.ylabel("Sales")
# plt.legend()
# plt.show()



# x =["Maths", "Hindi", "English", "Science", "S.S.T"]
# y1 = [10,20,25,35,45]
# y2 = [20,30,35,45,55]
# plt.plot(x, y1, label = 'Marks 2026', marker="o")
# plt.plot(x, y2, label = 'Marks 2026', marker="s")
# plt.title("Marks of Students 2024 & 2025")
# plt.xlabel("Subjects")
# plt.ylabel("Marks")
# plt.legend()
# plt.show()


#  ====================Bar Chart======================


# x = [1,2,3,4,5 ]
# y = [10, 20,25,35,45]

# plt.bar(x,y)
# plt.title( "Bar Chart ")
# plt.show()

# x = ["Ayush", "Jk", "Nobita", "Bheem", "Raju", "Doremone", "Jiyan", "Kaliya", "Deepak", "Harshit"]

# y = [10, 20,25,35,45, 55, 65, 75, 85, 95]
# colour = ["red", "orange", "pink", "pink","pink","pink","pink","pink","pink","green"]
# plt.bar(x,y, color = colour )
# plt.title("Bar Chart")
# plt.xlabel("Students")
# plt.ylabel("Scores")
# plt.show()



# data = [random.randint(1,100) for i in range(100)]
# plt.hist(data,bins = 5)
# plt.title("Histogram Example")
# plt.show()




# categories = ['A','B','C','D','E']
# sales = [10,20,55,35,45]
# plt.pie(sales, labels = categories,autopct = '%1.1f%%')
# plt.title("pie chart example")
# plt.show()
