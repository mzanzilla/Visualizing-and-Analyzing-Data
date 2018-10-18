import csv
file_name = "sitka_weather_07-2014.csv"
# Handle error if file is not available to be read
try:
    with open(file_name) as f:
        reader = csv.reader(f) #called once to store the first line of csv data in a list
        header_row = next(reader)
        print(header_row)
except IOError as err:
    print("File Error ", str(err))
