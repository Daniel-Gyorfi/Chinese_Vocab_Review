import io
from chinese import ChineseAnalyzer
import collections
from msvcrt import getch
import random

#opens file specified
fname = input("Lesson Filename: ")
content = ""
chinlyzer = ChineseAnalyzer()
f =open(fname, "r", encoding= "utf-8")
content = f.readlines()
vocab = {}
items = 0
#reads file line by line, using first token as key, rest as value
#term, definition
for line in content:
    parse = chinlyzer.parse(line).tokens()
    definition = ""
    for x in parse[2:]:
        if (x != '\n'):
            definition += x
    vocab[parse[0]] = definition
    items += 1
f.close()
#print(vocab)
#print(items)
guessed = 0
#iterating through random shuffle of dictionary
#shuffled = random.shuffle(list(vocab.keys()))
for key in vocab:
    print(vocab[key])
    #dummy loop to function as a hackneyed button prompt
    while (ord(getch()) != 13):
        guessed += 1
    print(key)
    


#print(content)
