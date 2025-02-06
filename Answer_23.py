# Take a string input from user and count the number of vowels and consonants using while loop and for loop both.

def number_of_vowels_using_for(sentence):
    print()
    vowels = 'aeiou'
    vowels_count = 0
    consonant_count = 0
    for char in sentence:
        if char in vowels:
            vowels_count += 1
        else:
            consonant_count += 1

    print(f"FOR: The number of vowels in sentence: {vowels_count}")
    print(f"FOR: The number of consonants in sentence: {consonant_count}")


def number_of_vowels_using_while(sentence):
    print()
    vowels = 'aeiou'
    vowels_count = 0
    consonant_count = 0
    i = 0

    while i < len(sentence):
        temp = sentence[i]
        if temp in vowels:
            vowels_count += 1
        else:
            consonant_count += 1
        i += 1

    print(f"WHILE: The number of vowels in sentence: {vowels_count}")
    print(f"WHILE: The number of consonants in sentence: {consonant_count}")


sentence = input("Enter a sentence: ").lower()
number_of_vowels_using_for(sentence)
number_of_vowels_using_while(sentence)


"""Output:
Enter a sentence: The witty fox jumps over the lazy dog

FOR: The number of vowels in sentence: 9
FOR: The number of consonants in sentence: 28

WHILE: The number of vowels in sentence: 9
WHILE: The number of consonants in sentence: 28
"""