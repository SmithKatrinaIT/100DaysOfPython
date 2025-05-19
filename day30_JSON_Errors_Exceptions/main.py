"""
	Concept: Handling Program Errors and Exceptions
	-- JSON is the most common structure of data

	-- "Catching Exceptions" is to catch the error before the programs fails
	-- Using a bare "except" is not best practice. It is too broad of a clause.
		-- A bare except clause (except without passing the exception to catch), when the "try" fails will ignore all errors. Meaning if there
		   are multiple types of errors in the "try" block, all will be "caught" in the (bare) except clause.
		   -- this is not the pratical behavior we should implement
		   -- If a known error will occur, we should specify that specific exception in the except clause
 	-- "raise" keyword: allows for raise our own exceptions; which will trigger the exception raised in the code
 		-- UseCase: when the code is valid but it yields the incorrect results
"""

# trying to read a file that doesn't exist in the specified path will throw a FILE_NO_FOUND error
try:
	file = open("a_file.txt")
except:
	# print("There was an error") <-- not useful in catching exceptions, but good for debugging
	# This is where we specify a good alternative if the "try" fails
	file = open("a_file.txt", "w") # passing the "w" write flag will create the file if it doesn't already exist and allow us to write to that file
	file.write("Write something")

try:
	file = open("b_file.txt")
	b_dictionary = {"key": "value"}
	print(b_dictionary["skfjadkls"]) # will throw a KeyError, but with a bare except clause, the error will be ignored and not handled gracefully
except:
	# This is where we specify a good alternative if the "try" fails
	file = open("b_file.txt", "w") # passing the "w" write flag will create the file if it doesn't already exist and allow us to write to that file
	file.write("Write something")


# Catch all expected errors by specifying them in the except claus(es)
try:
	file = open("c_file.txt")
	c_dictionary = {"key": "value"}
	print(c_dictionary["skfjadkls"])  # will throw a KeyError, but with a bare except clause, the error will be ignored and not handled gracefully
except FileNotFoundError:
	# This is where we specify a good alternative if the "try" fails
	file = open("c_file.txt", "w")  # passing the "w" write flag will create the file if it doesn't already exist and allow us to write to that file
	file.write("Write something")
except KeyError:
	print("That key does not exist")

# pass the error message back to user
try:
	file = open("d_file.txt")
	d_dictionary = {"key": "value"}
	print(d_dictionary["skfjadkls"])
	# will throw a KeyError, but with a bare except clause, the error will be ignored and not handled gracefully
except FileNotFoundError:
	# This is where we specify a good alternative if the "try" fails
	file = open("d_file.txt", "w")
	# passing the "w" write flag will create the file if it doesn't already exist and allow us to write to that file
	file.write("Write something")
except KeyError as error_msg:
	print("That key does not exist")

	# The exception usually has a message object associated with it that we can use to notify the user
	print(f"The key {error_msg} does not exist")


# use the 'else' clause when whatever the program is "try"ing all succeeds and no exceptions were thrown; what else does it need to do
try:
	file = open("e_file.txt")  # create the file beforehand so it exists at runtime and then the else block should execute print statement
	e_dictionary = {"key": "value"}
	print(e_dictionary["key"])  #change to valid key
	# will throw a KeyError, but with a bare except clause, the error will be ignored and not handled gracefully
except FileNotFoundError:
	# This is where we specify a good alternative if the "try" fails
	file = open("e_file.txt", "w")
	# passing the "w" write flag will create the file if it doesn't already exist and allow us to write to that file
	file.write("Write something")
except KeyError as error_msg:
	print("That key does not exist")

	# The exception usually has a message object associated with it that we can use to notify the user
	print(f"The key {error_msg} does not exist")

else:
	content = file.read()
	print(content)


# The 'finally' clause will run no matter what happens in the code blocks
try:
	file = open("f_file.txt")  # create the file beforehand so it exists at runtime and then the else block should execute print statement
	e_dictionary = {"key": "value"}
	print(e_dictionary["key"])  #change to valid key
	# will throw a KeyError, but with a bare except clause, the error will be ignored and not handled gracefully
except FileNotFoundError:
	# This is where we specify a good alternative if the "try" fails
	file = open("f_file.txt", "w")
	# passing the "w" write flag will create the file if it doesn't already exist and allow us to write to that file
	file.write("Write something else")
except KeyError as error_msg:
	print("That key does not exist")

	# The exception usually has a message object associated with it that we can use to notify the user
	print(f"The key {error_msg} does not exist")

else:
	content = file.read()
	print(content)

finally:
	file.close()
	print("File was closed.")


# Raise exception UseCase
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
	raise ValueError("Human Height should not be over 3 meters.")
bmi = weight / height ** 2
print(bmi)
