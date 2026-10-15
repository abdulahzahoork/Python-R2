# Count vowels
# Ask the user for a word and count how many vowels (a, e, i, o, u) it contains.
# Hint: Loop through each character in the word.


word = input("Enter a word: ").lower()
count = 0

for i in word: 
    if i in 'aeiou':
        count+=1

print(f"Vowel count: {count}")