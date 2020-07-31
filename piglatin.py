# Pig Latin Project
# mindnumb -> indnumbmay
# apple -> appleyay

# get sentence from user
original = input("What sentence would you like to translate to pig-latin? ").strip().lower()

# split sentence into words
words = original.split()

# loop through words and convert to pig latin
new_words = []

for word in words:
    if word[0] in "aeiou":
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        the_rest = word[vowel_pos:]
        new_word = the_rest + cons + "ay"
        new_words.append(new_word)

# stick words back together, the join method puts items in list together with a space in between
output = " ".join(new_words)

# output the final string
print(output)
