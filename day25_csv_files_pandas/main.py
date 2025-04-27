"""
Concept: Working with csv data and Panda
 -- Python built-in library for working with csv files: `import csv`
 -- data_file.reader() returns a csv.reader() object that can be looped through to extract each row of data in the file
    -- each row returned is a Python List object

-- Pandas is a Python data analysis library used to help with working with more complex tabular (csv) files
   -- 2 Data types in Pandas: Series and Dataframe
      -- Series (1-dimensional data) - equivalent to a column of data. Acts like a list
      -- Dataframe (2-dimensional data) - equivalent to the entire Excel/Google table (sheet - columns and rows)
"""

#open and read weather_data file
# with open("weather_data.csv") as data:
#
#     #data.read() will read each line. print(contents) will print to console each line
#     contents = data.read()
#     print(contents)
#
# with open("weather_data.csv") as data:
#     #data.readlines() reads one line at a time and returns a list of the lines read in. print(contentsList) will print the list of the lines in the file
#     #NOTE: once you read the file once - the reader is at the end of the file. Must re-open and re-read the file to get the contents again
#     contentsList = data.readlines()
#     print(contentsList)

""" Python built-in library for working with csv files: `import csv` """
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


""" Pandas must be installed (its not a built-in library: `import pandas <-- then click install package` 
    -- with pandas, the pandas.read_csv() method will open and read the csv file and format the data into a table form. 
       You don't have to use `with open()  or read() to open and read the file
"""
import pandas

data = pandas.read_csv("weather_data.csv")
#print(data)
#print(type(data))

#pandas identifies the header row.  With the headers identify, it easy to specify which column of data to extract
# Using the temperatures example above we can extract the temperatures with one line
#print(data["temp"])


# convert csv data to python dictionary. puts each column into a separate dictionary
data_dict = data.to_dict()
#print(data_dict)

# #convert panda series data in to a python list. Then you can perform any list functions(methods) on the native python list
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# # calculate the average temp from the extracted list of temperatures
# num_temp = len(temp_list)
# temp_sum = 0
# for temp in temp_list:
#     temp_sum += temp
# temp_avg = round((temp_sum / num_temp), 2)
# print(f"Long way to calculate Average temp: {temp_avg}")
#
# #short native python way to calculate average
# print(f"Using Python built-in mathematical methods to calculate Average temp:  {round(sum(temp_list) / len(temp_list), 2)}")
#
# #shortest way to calculate average temp using Panda methods
# print(f"Shortest way to calculate Average Temp using Pandas {round(data["temp"].mean(),2)}")
#
# #looking through Panda documentation to find a method to extract the max value from a Panda series/dataframe data structure
# #Panda Documentation Link:
# # -- https://pandas.pydata.org/docs/
# # -- https://pandas.pydata.org/docs/reference/series.html
#
# #using Pandas Series data to extract the max value in the structure
# max_temp = data["temp"].max()
# print(f"Max temp using Panda series data: {max_temp}")
#
# #Pandas: Get the column data: specify the name of the column which Panda extracts as the first row in the file by default
# #When you specify the column, you are access the Panda "series" data structure
# #Alternative to [] notation to extract the column data --- can use the . (dot) notation
# print(f"print data under the 'condition' column using dot notation:\n{data.condition}")
# print(f"print data under the 'condition' column using square bracket notation:\n{data['condition']}")


#Pandas: Get data in a Row --- get the data structure > specify the column > specify the column value > extract the row
#NOTE: will allow extract the column headers when you print the row
# row = data[data.day == 'Monday']
# print(row)
#
# #Challenge: Extract the row with the max weather temp
# max_temp = data["temp"].max()
# max_temp_row = data[data.temp == max_temp]
# print(f"Max temp row:\n{max_temp_row}")
#
# #Extract just a piece of the row data but accessing the column value first, then performing further Panda operations on it
# monday = data[data.day == "Monday"]
#
# print(f"Extract just a piece of the row data using the column object: {monday.condition}")
#
# #Challenge: Extract the Monday's temp and convert from Celsius to Fahrenheit
# #formula: (Celsius x 9/5) + 32
# monday_temp = monday.temp
# monday_temp_in_fahrenheit = (monday_temp * (9/5)) + 32
# print(f"Monday's Temp in Fahrenheit: {monday_temp_in_fahrenheit}")

#Create a Dataframe from scratch --- using a Python Dictionary
data_dict = {
    "students": ['Amy', 'Katrina', 'John'],
    "scores": [76, 56, 65]
}

panda_dataframe = pandas.DataFrame(data_dict)
print(panda_dataframe)

# convert the Dataframe to a csv. Call the .to_csv() method on the created Dataframe, takes in the path and name of the csv file including the .csv extension
panda_dataframe.to_csv("new_data.csv")





