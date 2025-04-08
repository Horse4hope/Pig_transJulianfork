Pig Latin is a pseudo-language that is created based on the construction of a word in
English.There are different rules to follow for words that start with a consonant, words that start
with a vowel, and words that contain the letter “y”.
● Words that start with a consonant
○ Add a “-” to the end of the word.
○ Move every consonant value before the first vowel to the end.
○ Add an “ay” to the end.
○ Example: fruit will turn into uit-fray
● Words that begin with vowels
○ Add a “-” to the end of the word.
○ Add one of “yay”, “way”, or “ay” to the end.
○ Example: Octopus turns into octopus-yay, octopus-way, or octopus-ay.
● Words that contain “Y”
○ If a word starts with Y
■ Follow the consonant rule and treat Y as a consonant.
○ If there are only consonants before Y at the beginning of the word
■ Move all consonants before Y to the end of the word and follow the
consonant rule.
Create a .py file that asks a user to enter a phrase that should be translated. Your program
should detect whether the phrase is in English or Pig Latin, and translate that word to the other
language. This should be tested with 3-5 words in each phrase for each language.
**Hint: You can use the isalpha() method
You should work with a partner on this project and decide how to split the work. Each partner
should have at least 5 commits and at least 5 pull requests on separate branches on their
respective repositories.

Expected sample output:
(program start)
Please enter a phrase to be translated:
I am translating to Pig Latin
English was detected. Translating to Pig Latin.
Translation: I-yay am-yay anslating-tray o-tay ig-Pay atin-Lay
Would you like to translate again? (Y/N)
Y
Please enter a phrase to be translated:
I-yay am-yay anslating-tray o-tay English-yay
Pig Latin was detected. Translating to English.
Translation: I am translating to English
Would you like to translate again? (Y/N)

(program end)
m-I thought the language was unclear, but its fine
