#!bin/python3
# ---- do not edit this section ----
print("preparing your variables...")
import my_functions as myf
nums = myf.getintlist("u11project/my_nums.txt")
words = myf.getstring("u11project/my_story.txt")
# --- do not edit above this line ---

print("\n--- part 1, becoming familiar with the data ---")
# TODO print 'nums' to see what you are dealing with, then comment out this line
# TODO print 'words' to see what you are dealing with, then comment out this line


# TODO what type of data is 'nums'? (print its type)
# TODO what type of data is 'words'? (print its type)



# TODO how many items are in 'nums'?
# TODO how many items are in 'words'?



# TODO print the first and last item in 'nums'
# TODO print the first and last item in 'words'



# TODO print an item near the middle of 'nums'
# TODO print an item near the middle of 'words'



# TODO use slicing to print the first 10 items in 'nums'
# TODO use slicing to print the last 10 items in 'words'



# TODO if 13 is in nums, print its index
# TODO if "computer" is in words, print its index





#---------- part 2, focus on 'nums' -----------------------
print("\n\n--- part 2, focus on 'nums' ---")
# The data for 'nums' was corrupted!
# the data should not have any numbers less than 10
# TODO count how many numbers are less than 10


# TODO create a new list with only items greater than or equal to 10



# TODO display how many items are in the list now



# TODO print the sum of the items in 'nums'
# TODO print the largest and smallest item in 'nums'
# TODO sort 'nums', display the first and last item to check your work from above



# now let's analyze the data
# we need to count how many times each number appears
# TODO make a list of tuples where each tuple is (i, count(i))
# hint: what are the min & max values? this is the range for 'i'




#---------- part 3 ------------------------------
print("\n\n--- part 3, focus on 'words' ---")
# cleansing the data
# TODO remove the newlines from the data
# TODO remove all punctuation 
# TODO convert to lowercase





words = words.split(" ")
# TODO what is different about the variable 'words' now compared to before? you may need to print a slice to see






# TODO count the number of words that end with 'ing'








#---------- final boss challenge ---------------------------
print("\n\n--- optional challenge ---")
# create a new list of words, without any duplicates
# find the most common word 


