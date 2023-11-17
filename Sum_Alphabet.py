#Define the main function sum_alphabet that takes a list of words as input
def sum_alphabet(words):
    #Define a nested fucntion alphabet_sum that calculates the alphabet sum for give word
    def alphabet_sum(word):
        #Sum of ordinal positions of each character in the lowercase version of the word
        return sum(ord(char) - ord('a') + 1 for char in word.lower())
    #Apply the alphabet_sum function to each word in the input list using the list comprehension
    #This creates a llist of alphabet sums for each word
    return [alphabet_sum(word) for word in words]
#Take input from user and split it into a list of words
user_input = input("Please Enter your string:")
words = user_input.split()
#Calculate the alphabet sum for the input list of words
output=(sum_alphabet(words))
#Print the resulting alphabet sum
print("The sum of the alphabets is:", output)