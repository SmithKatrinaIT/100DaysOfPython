'''
	CONCEPT: Data Exploration with Pandas

		NOTE: THIS LESSION WAS DONE ENTIRELY IN GOOGLE COLABORATORY VIA GOOGLE DRIVE.  BELOW ARE SOME NOTES ON THE COMMANDS USED

		-- Use a Google Colaboratory Notebook for the .cvs file

		-- Challenge Questions and Solutions

		1) Import statement
			import pandas as pd

		2) Read the .csv file and store it in a Pandas dataframe (change the default column names and remove csv header row)
			df = pd.read_csv('QueryResults.csv', names=['DATE', 'TAG', 'POSTS'], header=0)

				NOTE:  df is shorthand for "dataframe"

		3) Examine the first 5 rows and the last 5 rows of the of the dataframe
			df.head()  <-- first 5 rows
			df.tail()  <-- last 5 rows

		4) Check how many rows and how many columns there are. What are the dimensions of the dataframe?
			df.shape  <-- no () in this call.  It gives you the dataframe dimensions (rows, columns)

		5) Count the number of entries in each column of the dataframe
			df.count()

		6) Calculate the total number of post per language. Which Programming language has had the highest total number of posts of all time?
			df.groupby('TAG').sum()  <-- TAG is the column_name; sum() gives the number of posts each programming language had since creation of Stack Overflow
			df.groupby('TAG').count  <-- count() gives the entries per column; how many months of entries exist per programming language

		7) Use Pandas to change format from a string of "2008-07-01 00:00:00" to a datetime object with the format of "2008-07-01"
			df['DATE'] = pd.to_datetime(df['DATE'])  <-- using Pandas 'to_datetime() method to convert date string to date object

				NOTE: pd is our Panda object from above import statement

	DATA Manipulations

		1) Convert your DataFrame so that each category has its own column using Pandas .pivot() method.
			reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')

			NOTE: the index= is the categories for the rows
				  the columns= is the categories for the columns
				  the values= is what you want in the new cells

		2) Change the rows that have a NaN value. We can substitute the number 0 for each NaN value in the DataFrame.
			reshaped_df.fillna(0, inplace=True)  <-- using the .fillna() method.

		3) Check if there are any NaN values left in the entire
			reshape_df.isna().values.any()

		4) Replace NaN values after finding them with .isna()
			.fillna()


	DATA VISUALISATION WITH MATPLOTLIB

		1) import matplotlib.pyplot as plt

		2) Create a line graph of Java popularity of the months
			plt.plot(reshaped_df.index, reshaped_df.java)  <-- index is the months ('DATE') in the dataframe
			created (multiple) line charts using .plot() with a for-loop


			Styling the Chart

				Let's look at a couple of methods that will help us style our chart:

				.figure() - allows us to resize our chart

				.xticks() - configures our x-axis

				.yticks() - configures our y-axis

				.xlabel() - add text to the x-axis

				.ylabel() - add text to the y-axis

		3) Smoothing out Time-Series Data
			add a legend to tell apart which line is which by colour
			smoothe out our time-series observations with .rolling().mean() and plotted them to better identify trends over time.

'''