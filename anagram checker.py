# anagram checker
# check if two given words are anagrams of each other
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

new_word1 = word1.lower()
new_word2 = word2.lower()

if sorted(new_word1) == sorted(new_word2):
    print("The words are anagrams of each other")
else:
    print("The words are  not anagrams of each other")