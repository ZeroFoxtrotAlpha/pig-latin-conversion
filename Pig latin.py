def pig_latin_translation():
    string = input("Enter a string: ")
    words = string.split()

    translated_words = []
    for word in words:
        if word[0].lower() in 'aeiou':
            translated_word = word + "-way"
        else:
            translated_word = word[1:] + "-" + word[0] + "ay"
        translated_words.append(translated_word)

    translated_string = " ".join(translated_words)
    print("Translated string:", translated_string)

pig_latin_translation()