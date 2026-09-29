# Program to check whether a string is a palindrome

text = "madam"

# Remove spaces and ignore letter case
cleaned_text = text.replace(" ", "").lower()

if cleaned_text == cleaned_text[::-1]:
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")
