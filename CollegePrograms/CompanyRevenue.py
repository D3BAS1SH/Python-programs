""" import matplotlib.pyplot as PL

Months=["Jan","Feb","Mar","Apr"]
Revenue=[2.5,4.0,2.0,1.0]

PL.figure(figsize=(4,4))
PL.scatter(Months,Revenue,marker='o')
PL.xlabel("Months")
PL.ylabel("Revenue")
PL.title("Month Vs Revenue Graph.")

PL.pie(Revenue,labels=Months,autopct='%1.1f%%')
PL.axis("equal")

PL.grid(True)
PL.show()
 """
import matplotlib.pyplot as plt

# Define data
months = ["Jan", "Feb", "Mar", "Apr"]
revenue = [2.5, 4.0, 2.0, 1.0]

# Create the pie chart with values displayed inside portions (without percentage symbol)
plt.pie(revenue, labels=months, autopct="%.1f")  # Display values with one decimal place

# Set title
plt.title("Monthly Revenue")

# Equal aspect ratio for a circular pie chart
plt.axis("equal")  

# Show the plot
plt.show()
