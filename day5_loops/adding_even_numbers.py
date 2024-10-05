"""
Lesson 18: Adding Even Numbers in a Range of Numbers (Day 5 concepts)
 -- Loops, Range, and Code Blocks
 -- For Loop with Range function and 'step' argument
"""

target = int(input("Enter a number between 0 and 1000: ")) # Enter a number between 0 and 1000
# 🚨 Do not change the code above ☝️

# Write your code here 👇

sum_even = 0
for num in range(2, target + 1, 2):
    sum_even += num

print(sum_even)