# ---- do not edit this section ----
print("preparing your variables...")
import my_functions as myf
scores = myf.getintlist("u11project/act_data.txt")
words = myf.getstring("u11project/my_story.txt")
# --- do not edit above this line ---

print("\n--- part 1, becoming familiar with the data ---")
# TODO print 'scores' to see what you are dealing with, then comment out this line
# TODO print 'words' to see what you are dealing with, then comment out this line


# TODO what type of data is 'scores'? (print its type)
# TODO what type of data is 'words'? (print its type)



# TODO how many items are in 'scores'?
# TODO how many items are in 'words'?



# TODO print the first and last item in 'scores'
# TODO print the first and last item in 'words'



# TODO print an item near the middle of 'scores'
# TODO print an item near the middle of 'words'



# TODO use slicing to print the first 10 items in 'scores'
# TODO use slicing to print the last 10 items in 'words'



# TODO if 36 is in scores, print its index
# TODO if "computer" is in words, print its index





#---------- part 2, focus on 'scores' -----------------------
print("\n\n--- part 2, focus on 'scores' ---")
print("this data is the 2023 ACT scores from Missouri\n")
# TODO determine the average of 'scores' (remember: avg = sum/number_of_items)
# TODO print the largest and smallest item in 'scores'
# TODO sort 'scores', display the first and last item to check your work from above



# now let's analyze the data
# we need to count how many times each number appears
# TODO make a list of tuples where each tuple is (i, count(i))
# hint: what are the min & max values? this is the range for 'i'


# perform one more data analysis of your choice on 'scores'



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
# use this new list to help find the most common word in 'words' 


