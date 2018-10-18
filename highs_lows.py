import csv
from matplotlib import pyplot as plt
file_name = "sitka_weather_07-2014.csv"
# Handle error if file is not available to be read
with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader) #called once to store the first line of csv data in a list

    #print each header an it's position in the list for easy reading
    for index, columnheader in enumerate(header_row): #enumerate is used on list to get the index of each item as well as the value
        print(index, columnheader)

    #Read data from columns 0 and 1 in CSV file(Date and High Temperatures )
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)
    print (highs)

#Plot data
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(highs, c="red")
    plt.title("Daily High Temperatures, July 2014", fontsize=24)
    plt.xlabel("", fontsize=16)
    plt.tick_params(axis="", which="major", labelsize=16)
    plt.show()
