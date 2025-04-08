import re #this is a great way to start

def to_pig_latin(word):
    """Converts an English word to Pig Latin."""
    vowels = "AEIOUaeiou"

    if not word.isalpha():
        return word  # Leave punctuation as-is

    is_capitalized = word[0].isupper()
    original_word = word  # Save for special cases
    word = word.lower()

    # Words starting with vowels or 'y' acting as a vowel
    if word[0] in vowels or (word[0] == 'y' and len(word) > 1 and word[1] in vowels):
        pig_latin = word + "-yay"
    else:
        # Find the first vowel (treat 'y' as a vowel if not the first letter)
        match = re.search(r"[aeiouy]", word)
        if match:
            index = match.start()
            prefix = word[:index]
            stem = word[index:]
            pig_latin = stem + "-" + prefix + "ay"
        else:
            pig_latin = word  # No vowels found

    # Handle capitalization
    if is_capitalized:
        parts = pig_latin.split("-")
        if len(parts) == 2:
            before_dash, after_dash = parts
            # Special handling if the original word is a single capital letter (like "I")
            if len(original_word) == 1:
                pig_latin = original_word + "-yay"
            else:
                pig_latin = before_dash + "-" + after_dash.capitalize()

    return pig_latin

def from_pig_latin(word):
    """Converts a Pig Latin word back to English."""
    if "-" not in word:
        return word  # If no hyphen, assume it's already English

    parts = word.split("-")
    if len(parts) != 2:
        return word  # Invalid Pig Latin structure, return as is

    root, suffix = parts
    if suffix in ["yay", "way", "ay"]:
        return root  # If it was a vowel-starting word
    elif suffix.endswith("ay"):
        return suffix[:-2] + root  # Convert back to English

    return word  # Return unchanged if format is unexpected

def detect_language(phrase):
    """Detects whether the phrase is in English or Pig Latin."""
    words = phrase.split()
    if all("-" in word and (word.endswith("ay") or word.endswith("yay") or word.endswith("way")) for word in words):
        return "Pig Latin"
    return "English"

def translate_phrase(phrase):
    """Translates a phrase between English and Pig Latin."""
    language = detect_language(phrase)
    words = phrase.split()

    if language == "English":
        translated_words = [to_pig_latin(word) for word in words]
        print("English detected. Translating to Pig Latin.")
    else:
        translated_words = [from_pig_latin(word) for word in words]
        print("Pig Latin detected. Translating to English.")

    return " ".join(translated_words)

def main():
    """Main loop for user interaction."""
    print("Program started!")  # Add this line to confirm script is running
    while True:
        phrase = input("Please enter a phrase to be translated:\n").strip()
        if not phrase:
            print("You entered an empty phrase. Please try again.")
            continue
        
        translation = translate_phrase(phrase)
        print("Translation:", translation)
        
        again = input("Would you like to translate again? (Y/N)\n").strip().lower()
        if again != 'y':
            print("Goodbye.")
            break

if __name__ == "__main__":
    main()
