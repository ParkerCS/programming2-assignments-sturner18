# SIMONE TURNER - PROGRAMMING 2
# imports
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
# List for each month
total_monthly_visitors = []

january = [int(x[1]) for x in data]
january = sum(january)
total_monthly_visitors.append(january)

february = [int(x[2]) for x in data]
february = sum(february)
total_monthly_visitors.append(february)

march = [int(x[3]) for x in data]
march = sum(march)
total_monthly_visitors.append(march)

april = [int(x[4]) for x in data]
april = sum(april)
total_monthly_visitors.append(april)

may = [int(x[5]) for x in data]
may = sum(may)
total_monthly_visitors.append(may)

june = [int(x[6]) for x in data]
june = sum(june)
total_monthly_visitors.append(june)

july = [int(x[7]) for x in data]
july = sum(july)
total_monthly_visitors.append(july)

august = [int(x[8]) for x in data]
august = sum(august)
total_monthly_visitors.append(august)

september = [int(x[9]) for x in data]
september = sum(september)
total_monthly_visitors.append(september)

october = [int(x[10]) for x in data]
october = sum(october)
total_monthly_visitors.append(october)

november = [int(x[11]) for x in data]
november = sum(november)
total_monthly_visitors.append(november)

december = [int(x[12]) for x in data]
december = sum(december)
total_monthly_visitors.append(december)

print(total_monthly_visitors)

# Make a BAR GRAPH with the total visitors on the y and month on the x.
plt.figure(1, figsize=(10, 5), tight_layout=True, facecolor='pink')
plt.bar(month_number, total_monthly_visitors, color='red')

# label the x with the month.  Rotate the text so we can read it.  (see example problem).  Use the tight_fit command to show all text.
plt.xlabel("Month")
plt.ylabel("Total Visitors")
plt.xticks(month_number, month_names, rotation=45)

# label axes, title the graph as necessary.
plt.title("Total Visitors to Chicago Library each Month in 2017")


# MATPLOTLIB PROBLEM # 2 
# Chicago Public Transit Usership Graph (20pts)
# go to https://data.cityofchicago.org/Transportation/CTA-Ridership-Annual-Boarding-Totals/w8km-9pzd
# download the CTA ridership data as a csv.
# Read the data into a list using the csv library.
with open("files/CTA_-_Ridership_-_Annual_Boarding_Totals.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)

# list of years
year_names = [x[0] for x in data][1:]
print(year_names)

year_numbers = [x for x in range(len(year_names))]
print(year_numbers)

# list of bus numbers
bus = [x[1] for x in data][1:]
bus = [int(x) for x in bus]

# list of paratransit
paratransit = [x[2] for x in data][1:]
paratransit = [int(x) for x in paratransit]

# list for rail
rail = [x[3] for x in data][1:]
rail = [int(x) for x in rail]

# list for total
total = [x[4] for x in data][1:]
total = [int(x) for x in total]

# Make a plot of paratransit, bus, rail, and total numbers by year (all on the same graph)
plt.figure(2, tight_layout=True)

plt.plot(year_numbers, bus, label="Bus")
plt.plot(year_numbers, paratransit, label="Paratransit")
plt.plot(year_numbers, rail, label="Rail")
plt.plot(year_numbers, total, label="Total")
plt.xticks(year_numbers, year_names, rotation=45)

plt.legend(bbox_to_anchor=(0, 1), loc="upper left")

# Make each line, points, and color different for the four graphs.
# Make a legend to identify each line.
# Label axes and give your graph a title.  Change it in any other way you see necessary to give it a clean look.
plt.xlabel("Years")
plt.ylabel("Transit Boarding Totals")
plt.title("CTA Ridership Annual Boarding Totals")
plt.show()