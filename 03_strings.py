# Python Fundamentals - String Programs

# 1. Palindrome string (ignore spaces and case)
word = input("Enter a string: ")
clean_word = word.replace(" ", "").lower()

if clean_word == clean_word[::-1]:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")


# 2. Find the longest word in a sentence
sentence = input("\nEnter a sentence: ")
words = sentence.split()

if words:
    longest_word = words[0]
    for item in words:
        if len(item) > len(longest_word):
            longest_word = item
    print("Longest word:", longest_word)
else:
    print("No words entered.")


# 3. Check whether two strings are anagrams
first = input("\nEnter first string: ")
second = input("Enter second string: ")

first_clean = first.replace(" ", "").lower()
second_clean = second.replace(" ", "").lower()

if sorted(first_clean) == sorted(second_clean):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


# 4. Remove duplicate characters while maintaining order
text = input("\nEnter a string: ")
result = ""

for character in text:
    if character not in result:
        result += character

print("After removing duplicates:", result)


# 5. Compress a string, for example aaabbc -> a3b2c1
text = input("\nEnter a string to compress: ")

if text == "":
    print("Compressed string: ")
else:
    compressed = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + str(count)
            count = 1

    compressed += text[-1] + str(count)
    print("Compressed string:", compressed)
