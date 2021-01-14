# M4-lab encoding a phrase
# J.Casteel
# 11/18/2020

print('\n')
#### The usual pleasantries ####
sep = '*'*60


def displayInro():
    mess = sep+'''
This Program takes a string and encodes it by taking each
characters starting lexicographical position and shifting
it by (StartingPosition - 65 + shift ) % 26 + 65.

The user will enter a phrase and then enter an amount to
shift by and the program will return the original phrase,
the encoded phrase, and the decoded phrase.
'''
    print(mess)


def displayTermination():
    mess = '\n'+sep+'''
This program is now terminating!
'''+sep+'\n'
    print(mess)

#### define cypher and encode ####


def encodedPhrase(phrase, shift):
    print('Original Phrase:  {}'.format(phrase))
    coded_phrase = ''
    for letter in phrase:
        val = ord(letter)
        val = ((val - 32 + shift) % 95) + 32
        coded_phrase += chr(val)
    print("   Coded Phrase:  {}".format(coded_phrase))

#### define cypher and encode then decode ####


def decodedPhrase(phrase, shift):
    coded_phrase = ''
    decoded_phrase = ''
    for letter in phrase:
        val = ord(letter)
        val = ((val - 32 + shift) % 95) + 32
        coded_phrase += chr(val)
    for letter in coded_phrase:
        val = ord(letter)
        val = ((val - 32 - shift) % 95) + 32
        decoded_phrase += chr(val)
    print(" Decoded Phrase:  {}".format(decoded_phrase))

#### User Inputs ####


def enterInt():
    prompt = sep+'''
Please enter a shift as an integer:
For a shift of 12 , enter 12
--> '''
    print(prompt, end="")
    enteredNumber = eval(input())
    return enteredNumber


def enterPhrase():
    prompt = sep+'''A
Please enter a phrase:
for Hello World, simply enter Hello World
--> '''
    enteredPhrase = '{}'.format(input(prompt))
    return enteredPhrase


#### Execute ####
displayInro()
shiftInput = enterInt()
phraseInput = enterPhrase()
print('\n'+sep+'\n')
encodedPhrase(phraseInput, shiftInput)
decodedPhrase(phraseInput, shiftInput)
displayTermination()
