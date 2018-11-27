def genchain_(result,words):
    possible_words = [word for word in words if word not in result and word[0]==result[-1][-1]]
    return possible_words

def get_paths(paths, words):
    tot=[]
    for path in paths:
        possible_words = genchain_(path,words)
        if not(possible_words==[]):
            tot.extend(get_paths([path+[word] for word in possible_words],words))
        else:
            tot.append(path)
    return tot
def genchain(word,func=max):
    words = sorted(open('animals.txt','r').read().split('\n'))
    words.remove('')
    return func(get_paths([[word]],words), key=len)
