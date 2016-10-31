# -*- coding:utf-8 -*-
import random
from urllib import request
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
"class ###(###):":
"Make a class named ### that is-a ###.",
"class ###(object):\n\tdef __init__(self, ***)" :
"class ### has-a __init__ that takes self and *** parameters.",
"class ###(object):\n\tdef ***(self, @@@)":
"class ### has-a function named *** that takes self and @@@ parameters.",
"*** = ###()":
"Set *** to an instance of class ###.",
"***.***(@@@)":
"From *** get the *** function, and call it with parameters self, @@@.",
"***.*** = '***'":
"From *** get the *** attribute and set it to '***'."
}

PHRASES_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASES_FIRST = True

for word in request.urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

#print(WORDS)



def convert(snippet, phrase):
    class_name = [w.capitalize() for w in random.sample(WORDS, snippet.count("###"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1, 3)
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        results = sentence

        for word in class_name:
            results = results.replace("###", word, 1)

        for word in other_names:
            resluts = results.replace("@@@", word, 1)
    return results

print(convert(WORDS, PHRASES))