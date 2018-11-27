
def chain(start,target):
    with open('wordslist-7.txt') as wordslist:
        wordslist=wordslist.read().split()
        def get_successors(elem):
            nonlocal wordslist
            return list(set([elem[:i]+chr(y)+elem[i+1:] for i in range(0,len(elem)) for y in range(ord('a'),ord('z')) if elem[:i]+chr(y)+elem[i+1:] in wordslist]))
        def get_paths(path, end):
            succ = get_successors(path[-1])
            tot=[]
            for s in succ:
                tot.extend((get_paths(path+[s],end) if s not in path else []) if s!=end else [path+[s]])
            return tot
        return '\n'.join(map(str,get_paths([start],target)))

import itertools

def chain(start,target):
    with open('dict.txt') as wordslist:
        wordslist=wordslist.read().split()
        def get_succ(word):
            nonlocal wordslist, target
            return list(set([word[0:j]+chr(i)+word[j+1:] for j in range(0,len(word)) for i in range(ord('a'),ord('z')) if (word[0:j]+chr(i)+word[j+1:] in wordslist)]))
        def get_path(path):
            nonlocal target
            tot = []
            for s in get_succ(path[-1]):
                tot.extend((get_path(path+[s]) if (s not in path) else []) if s!=target else [path+[target]])
            return tot
        return '\n'.join(map(str,get_path([start])))


print(chain("sailing", "writing"))
