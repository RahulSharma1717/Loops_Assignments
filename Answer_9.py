# Write a Python program that asks the user to enter a sentence and then prints the number of vowels in the sentence.

def number_of_vowels():
    sentence = input("Enter a sentence: ").lower()
    vowels = 'aeiou'
    vowels_count = 0
    for char in sentence:
        if char in vowels:
            vowels_count += 1

    print(f"The number of vowels in sentence: {vowels_count}")

number_of_vowels()


"""Output:
Enter a sentence: rtyuio dfghjk cvbnm, plkmn ' ][poiu 
The number of vowels in sentence: 6
"""


