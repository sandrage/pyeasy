import itertools

def get_possible_next(elem,wordslist):
    return list(set([elem[:i]+chr(y)+elem[i+1:] for i in range(0,len(elem)) for y in range(ord('a'),ord('z')) if elem[:i]+chr(y)+elem[i+1:] in wordslist]))


def create_chain(start_word,end_word,path,wordlist):
    path=path+[start_word]
    print(path)
    paths = []
    for word in get_possible_next(start_word,wordlist):
        if((word not in path) and (word!=end_word)):
            paths_generated= create_chain(word,end_word,path,wordlist)
            paths.extend(paths_generated)

        if word==end_word:
            paths.extend([path+[word]])
    return paths

def chain(start_word,end_word):
    with open("dict.txt") as fileopened:
        wordlist = fileopened.read()
        return '\n'.join(map(str,sorted(create_chain(start_word,end_word,[],wordlist))))

print(chain("sailing", "writing"))
