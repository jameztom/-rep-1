word = input("Enter the string:")
word_lower = word.lower()
if word_lower == word_lower[::-1]:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
