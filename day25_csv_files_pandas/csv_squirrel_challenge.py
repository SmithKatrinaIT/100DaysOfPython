"""Challenge:
    -- Use the Panda Library to:
        --extract the color of squirrels from the csv file
        -- extract the total number of squirrels by color
        -- save this data in a new csv file
"""
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#get the color series (column)
squirrel_colors = data["Primary Fur Color"]
grey_squirrels = data[data["Primary Fur Color"] == 'Gray']
cinnamon_squirrels = data[data["Primary Fur Color"] == 'Cinnamon']
black_squirrels = data[data["Primary Fur Color"] == 'Black']

# num_gray_squirrels = grey_squirrels.count()
# num_cinnamon_squirrels = cinnamon_squirrels.count()
# num_black_squirrels = black_squirrels.count()

num_gray_squirrels = len(grey_squirrels)
num_cinnamon_squirrels = len(cinnamon_squirrels)
num_black_squirrels = len(black_squirrels)


print(f"Number of Gray Squirrels: {num_gray_squirrels}")
print(f"Number of Cinnamon Squirrels: {num_cinnamon_squirrels}")
print(f"Number of Black Squirrels: {num_black_squirrels}")


"""Construct a new Dataframe and save to csv file """

# first create a Python Dictionary
squirrel_dict = {
     "Fur Color": ["Gray", "Cinnamon", "Black"],
     "Count": [num_gray_squirrels, num_cinnamon_squirrels, num_black_squirrels]
 }

# create the dataframe
squirrel_dataframe = pandas.DataFrame(squirrel_dict)

# save to csv
squirrel_dataframe.to_csv("squirrel_stats.csv")



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