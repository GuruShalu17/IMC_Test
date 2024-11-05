# Prompt the user to enter a sentence
# and then print the sentence in uppercase letters.

sentence = input("Please enter a sentence: ")
print(sentence.upper())


# Prompt the user to enter a paragraph and
# then count the number of words in the paragraph.

paragraph = input("Please enter a paragraph: ")
word_count = len(paragraph.split())
print(f"The paragraph has {word_count} words.")


# Prompt the user for a string,
# and check if all the characters in the string are digits. Output true or false

string = input("Please enter a string: ")
if string.isdigit():
    print("True")
else:
    print("False")


# Prompt the user for a string,
# and replace all occurrences of the letter "a" with the letter "o".

another_string = input("Please enter another string: ")
print(another_string.replace("a", "o"))


# Prompt the user to enter their full name and then print their initials.
# Assume that the user will enter their full name with a space between each name.

full_name = input("Please enter your full name: ")
initials = ""
for name in full_name.split():
    initials += name[0].upper()

print(f"Your initials are: {initials}")


# Prompt the user for a string,
# then print its length.

total_string = input("Please enter one more string: ")
length_string = len(total_string)
print(f"The length of your string is: {length_string}")
