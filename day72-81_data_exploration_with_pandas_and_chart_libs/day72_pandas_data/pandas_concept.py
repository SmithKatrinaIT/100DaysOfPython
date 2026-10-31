'''
	CONCEPT: Data Exploration with Pandas

		NOTE: THIS LESSION WAS DONE ENTIRELY IN GOOGLE COLABORATORY VIA GOOGLE DRIVE.  BELOW ARE SOME NOTES ON THE COMMANDS USED

		-- Use a Google Colaboratory Notebook for the .cvs file

			-- In Colaboratory Notebook: import pandas
				--Notebook commands:
					dataframe = panda.read.csv('csv_filename')
					dataframe.head() - show first 5 rows of the dataframe
					dataframe.tail() - show last 5 rows of the dataframe
					dataframe.shape - tells you the number of rows, columns in the dataframe
					dataframe.columns - tells you the column (field) names
					dataframe.isna()
					dataframe.findna(): find NaN values
					dataframe.dropna() - clean up dataframe

					-- Access columns data by using square brackets
						dataframe['Column_Name']
						-- Commands:
							-- .max() or .min(): for the "MAX/MIN" value within the column use ie. dataframe['column_name'].max()
							-- .idxmax() or idxmin: give you the index number for the row with the largest value
							-- .loc[index]: the value for that particular cell [column_name][index_num] does the same thing

							-- sort_values('Column_name', ascending=False/True)
							-- insert() to add new columns
							-- groupby(): aggregate data
								dataframe.groupby('Column_name').count()
							-- .mean(): get the average salary by group
								dataframe.groupby('Column_name').mean()




'''