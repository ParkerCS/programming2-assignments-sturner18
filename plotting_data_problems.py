# SIMONE TURNER
import csv
import matplotlib.pyplot as plt

# MATPLOTLIB PROBLEM # 1

# Chicago Public Library Computer Usage (15pts)
# open and read in the "Libraries_-_2018_Visitors_by_Location.csv" file into a list (use file located in the file folder, read in using csv library).
with open("files/Libraries_-_2017_Visitors_by_Location.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

# calculate (and make a list of) the total visitors to Chicago libraries each month.
month_names = data.pop(0)[1:-1]
print(month_names)

month_number = [x for x in range(12)]
print(month_number)

# Do not plot every library individually.  Instead, find the total for all libraries each month and plot that.
total_monthly_visitors = [x for x in data]

# Make a BAR GRAPH with the total visitors on the y and month on the x.
plt.figure(1, facecolor='pink')
plt.bar(month_number, total_monthly_visitors, color='red')

# label the x with the month.  Rotate the text so we can read it.  (see example problem).  Use the tight_fit command to show all text.
plt.xlabel("Month")
plt.ylabel("Total Visitors")
plt.xticks(month_number, month_names, rotation=90)

# label axes, title the graph as necessary.
plt.title("Total Visitors to Chicago Library each Month in 2017")


# MATPLOTLIB PROBLEM # 2 
# Chicago Public Transit Usership Graph (20pts)
# go to https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
# download the CTA ridership data as a csv.
# Read the data into a list using the csv library.
# Make a plot of paratransit, bus, rail, and total numbers by year (all on the same graph).
# Make each line, points, and color different for the four graphs.
# Make a legend to identify each line.
# Label axes and give your graph a title.  Change it in any other way you see necessary to give it a clean look.
