import csv
from matplotlib import pyplot as plt
from datetime import datetime
file_name = "sitka_weather_07-2014.csv"
# Handle error if file is not available to be read
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader) #called once to store the first line of csv data in a list

    #print each header an it's position in the list for easy reading
    for index, columnheader in enumerate(header_row): #enumerate is used on list to get the index of each item as well as the value
        print(index, columnheader)

    #Read data from columns 0, 1, 3 in CSV file(Date, High Temperatures, and low temperatures )
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        high = int(row[1])
        low = int(row[3])
        highs.append(high)
        lows.append(low)
        dates.append(current_date)
    print (highs)   #Print to show data is displaying correctly

#Plot data
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(dates, highs, c="red", alpha=0.5)
    plt.plot(dates, lows, c="blue", alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
    plt.title("Daily High and Low Temperatures, July 2014", fontsize=24)
    fig.autofmt_xdate()
    plt.ylabel("Temperature(F)")
    plt.xlabel("", fontsize=16)
    plt.tick_params(axis="", which="major", labelsize=16)
    plt.show()
