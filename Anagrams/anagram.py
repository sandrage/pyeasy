import functools
def hash(w):
  return ''.join(sorted(w.lower()))

def organize(alltext):
    words = {}
    for w in alltext:
        h = hash(w)
        if h in words:
            words[h]+=[w]
        else:
            words[h]=[w]
    return words
def anagrams():
    with open("wordlist.txt") as fileopened:
        alltext = fileopened.read().split('\n')
        return '\n'.join(list(map(lambda x: x[0]+" :- "+','.join(sorted(x[1:])),[w for w in organize(alltext).values() if len(w)>2])))

def anagram(word):
    with open("wordlist.txt") as fileopened:
        alltext = fileopened.read().split('\n')
        result = []
        word_hashed = hash(word)
        for w in alltext:
            h=hash(w)
            if h==word_hashed and w!=word: result+=[w]
        return sorted(result[1:],key=lambda a:a.lower())
