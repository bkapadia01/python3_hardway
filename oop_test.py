import random
from urllib.request import urlopen
import sys
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


word_url = "https://learncodethehardway.org/words.txt"
words = []

phrases = {
    "class %%%{%%%}:":
        "make a clase named %%% that is a %%%",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has a __init__ that takes self and *** params:",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has a function *** that takes self and @@@ params:",
    "*** = %%%()":
        "set *** to an instance of class %%%",
    "***.***(@@@)":
        "from *** get the *** function, call it with the params self and @@@",
    "***.*** = '***'":
        "from *** get the *** attributes and set it to '***'"
    }

# do they want to drill phrases first?
# this checks for the arugmetns in the terminal if there is 2 arguments (phython3.6 file name cass)
# if user types in exactly "english" as the 2nd arugment then it will run phrase_first = true
# this means that it will provide the phrase and user enters snippet
# else default is user enters snippet based on phrase
if len(sys.argv) == 2 and sys.argv[1] == 'english':
    phrase_first = True
else:
    phrase_first = False

#load up the words form the website, and create a list of words
for word in urlopen(word_url).readlines():
    words.append(str(word.strip(), encoding="utf-8"))

# fucntion name is convert
# this takes snippet and phrase from phrases dictonary above 
# snippet and phrase are from the function below (snippets = list(phrases.keys() and 
# phrase is frome the object of the snippet key phrase = phrases[snippet])

def convert(snippet, phrase):
    #capatalize the first letter for class names
    class_names = [w.capitalize() for w in 
                   random.sample(words, snippet.count("%%%"))]
    # selcts a random word for otehr name that can be eitehr fucntion name or params name
    other_names = random.sample(words,snippet.count("***"))
    #store valeus in array below
    results = []
    param_names = []

    for i in range (0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(words, param_count)
        ))

    for sentence in snippet, phrase:
        result = sentence[:]

        #replace class name placehoder with random word and store in select
        for word in class_names:
            result = result.replace("%%%", word, 1)

        #fake other names
        for word in other_names:
            result = result.replace("***", word, 1)
        
        #fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

#keep ging until they hit ctlr-D
try:
    while True:
        #from the phrases diction list all the keys
        snippets = list(phrases.keys())
        random.shuffle(snippets)
        for snippet in snippets:
            phrase = phrases[snippet]
            question, answer = convert(snippet, phrase)
            if phrase_first:
                    question, answer = answer, question
    
            print(question)
            input(">")
            print(f"answer: {answer} \n")
    
except EOFError:
    print("\nBYE!")
