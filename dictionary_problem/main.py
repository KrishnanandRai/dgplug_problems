import re
from collections import Counter
import sys


def words(text): return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('big.txt').read()))

def P(word, N=sum(WORDS.values())): 
    "Probability of `word`."
    return WORDS[word] / N

def correction(word): 
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word): 
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): 
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word):
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): 
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))


def parse_dictionary(dictionary):
    dic = {}
    with open(dictionary, 'r') as f:
        for line in f:
            try:
                li = line.split(' ', 1)
                word = li[0]
                meaning = li[1]
                if word not in dic:
                    dic[word] = meaning
            except:
                pass
    return dic



def search_word(word):
    word = word.title()
    dic = parse_dictionary('dictionary.txt')
    if word in dic:
        print(dic[word])
    else:
        nearest = correction(word)
        print("did you mean " + nearest)
        if nearest.title() in dic:
            print(dic[nearest.title()])
        else:
            print("Word not found!") 

 
if __name__ == "__main__":
    search_word(sys.argv[1])
