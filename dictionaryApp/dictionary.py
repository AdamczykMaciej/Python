"""This program serves as a dictionary"""
import json
import difflib
#from difflib import SequenceMatcher
from difflib import get_close_matches
#loads dictionary data, phrases
data = json.load(open("data.json"))
#dictionary functionality
def search(word):
    word = word.lower()
    if word in data:
        answer=""
        for i in data[word]:
            answer+=i.rstrip("[]\"")+"\n"
        return "\n"+answer
    #dictionary hints:
    matches=get_close_matches(word,data.keys(), cutoff=0.7)
    numOfMatches=len(matches)
    if numOfMatches==1:
        return "Did you mean %s instead?" % (matches[0])
    elif numOfMatches==2:
        return "Did you mean %s, %s instead?" % (matches[0], matches[1])
    elif numOfMatches==3:
        return "Did you mean %s, %s, %s instead?" % (matches[0], matches[1], matches[2])
    elif numOfMatches>=4:
        return "Did you mean %s, %s, %s, %s instead?" % (matches[0], matches[1], matches[2], matches[3])
    else:
        return "The word doesn't exist. Please double check it."
word = input("Enter a word: ")
print(search(word))
