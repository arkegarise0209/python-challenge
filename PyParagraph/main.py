#Dependencies
import os
import string

#Join file paths based on user input for file selection
file_name = input("Please enter file name: ")
file = os.path.join("raw_data", file_name)


#Read in the needed text file
with open(file, "r") as txt_file:
    paragraph = txt_file.read()

#Split text file into individual words
word_list = paragraph.split(" ")

#Count total words
word_count = len(word_list)

#Split text file into individual sentences
sentence_list = paragraph.split(".")

#Count total sentences 
sentence_count = (len(sentence_list) - 1)

#Loop through word_list and add the letter count of each word to total_letters
total_letters = 0
for word in word_list:
    total_letters += len(word)

#Divide total amount of letters by total amount of words to calculate average letter count per word
letter_count = (total_letters/word_count)


#Divide total amount of words by total amount of sentences to calculate average sentence length  
sentence_length = (word_count/sentence_count)

#Display Output
print("'''")
print("Paragraph Analysis")
print("---------------------")
print("Approximate Word Count:" + str(word_count))
print("Approximate Sentence Count:" + str(sentence_count))
print("Average Letter Count:" + str(letter_count))
print("Average Sentence Length:" + str(sentence_length))
print("'''")


#Output Files 
output_file = os.path.join("paragraph_analysis.txt")

with open(output_file, "w",newline="") as txt_file:
    txt_file.write("'''")
    txt_file.write("\n")
    txt_file.write("Paragraph Analysis")
    txt_file.write("\n")
    txt_file.write("---------------------")
    txt_file.write("\n")
    txt_file.write("Approximate Word Count:" + str(word_count))
    txt_file.write("\n")
    txt_file.write("Approximate Sentence Count:" + str(sentence_count))
    txt_file.write("\n")
    txt_file.write("Average Letter Count:" + str(letter_count))
    txt_file.write("\n")
    txt_file.write("Average Sentence Length:" + str(sentence_length))
    txt_file.write("\n")
    txt_file.write("'''")







