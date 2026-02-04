# write a program to count vowels, consonants, digits, words, and symbol in given list
string = "Hello123 Everyone45 MY67 name89 is0 Jattu Parmar.@#"
vowels = 0
consonants = 0
digits = 0
words = 1
symbols = 0
for char in string:
    if char.isalpha():
        if char.lower() in 'aeiou':
            vowels = vowels + 1
        else:
            consonants =  consonants + 1
    elif char.isdigit():
        digits = digits + 1
    elif char.isspace():
        words = words + 1
    else:
        symbols = symbols + 1
print("Total number of vowels in the string:", vowels)
print("Total number of consonants in the string:", consonants)
print("Total number of digits in the string:", digits)
print("Total number of words in the string:", words)
print("Total number of symbols in the string:", symbols)

