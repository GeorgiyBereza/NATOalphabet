import sys

import pandas

csv_source = pandas.read_csv("nato_phonetic_alphabet.csv")
print("This is NATO phonetic alphabet")
print(csv_source)
nato_alphabet = {}

#Looping through rows of a data frame
for (index, row) in csv_source.iterrows():
    nato_alphabet.update({row.letter:row.code})

def convert_to_nato_alphabet(word):
    return [nato_alphabet.get(letter) for letter in word]

while True:
    print("Enter a word (or exit):")
    message = input().upper()
    if message == "EXIT":
        sys.exit()
    else:
        message = message.split()
        for line in message:
            print(f"{line} : {convert_to_nato_alphabet(line)}")


