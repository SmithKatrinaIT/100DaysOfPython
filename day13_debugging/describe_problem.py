"""
Concept: Debugging Code - Describe the Problem
"""

############DEBUGGING#####################

# # Describe Problem
# '''Problem:
#     for loop that loops through a range of numbers from 1 to 19 because 20 is excluded
#     the conditional is checking if whatever the value of i is in the loop is 20 to print out a message
#     Issue:  i will never get to 20 because 20 is NOT included in the range
# '''
# def my_function():
#   #for i in range(1, 20): # the error
#   for i in range(1, 21):  # the fix
#     if i == 20:
#       print("You got it")
# my_function()
#
#
# # Reproduce the Bug
# '''Problem
#     a list of strings as the disce_imgs
#     random number between 1 and 6
#     Issue: when dice_num == 6 program will throw a IndexError because list indexes start at zero not one.
# '''
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# # dice_num = randint(1, 6) # error
# #dice_num = 6 # reproduce the error
# dice_num = randint(0, 5) # the fix
# print(dice_imgs[dice_num])
#
#
# # Play Computer
# '''Problem
#     ask you for your year of birth
#     if year is  greater than 1980 and less than 1994; print message
#     if year is greater than 1994 print message
#     Issue: doesn't account for if year is equal to 1980 or equal to 1994 so nothing will print or if you were born before 1980
# '''
# year = int(input("What's your year of birth?"))
# # if year > 1980 and year < 1994: # missing logic
# if year >= 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
#
# # Fix the Errors
# '''Problem:
#     conditional statement that asks the user for their age.
#     Issue: the conditional statement is not properly indented; compare an integer with a string; also print statement not formatted as 'f' string
# '''
# #age = input("How old are you?") - error
# age = int(input("How old are you?")) # fix
# if age > 18:
# #print("You can drive at age {age}.") - error
#   print(f"You can drive at age {age}.") # fix


# #Print is Your Friend
# '''Problem:
#     calculate the total words based on the number of pages and number of words per page
#     Issue: pages and word_per-page is re-defined - only need once declaration & assignment; word_per_page using the wrong assignment operator so the calculation returns 0
# '''
# # pages = 0 - unnecessary
# # word_per_page = 0
# pages = int(input("Number of pages: "))
# # word_per_page == int(input("Number of words per page: ")) - error
# word_per_page = int(input("Number of words per page: ")) # fix
# total_words = pages * word_per_page
# print(total_words)



# Use a Debugger
'''Problem:
    function that takes in a list and multiplies each element in the list by 2 then append each element to another list and prints the second list
    Issue: the second list is outside the for loop therefore elements from listA never get appended to listB
'''
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
  #b_list.append(new_item) - error
    b_list.append(new_item) # fix (indent)
  print(b_list)

mutate([1,2,3,5,8,13])