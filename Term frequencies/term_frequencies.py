import sys, re

def freqs(filename, number):
    with open(filename) as file:
        fulltext = file.read()
        words = filter_text(fulltext)
        unique = set(words)
        unique.discard('')
        return sorted([(term, words.count(term)) for term in unique if words.count(term) >= number], key=lambda x: x[1], reverse=True)
def remove_not_alpha(word):
    return ''.join(filter(lambda y : y.isalnum(), word))
def filter_text(fulltext):
    words = re.split('\s',fulltext)
    return list(map(lambda x : str.lower(remove_not_alpha(x)),words))

if __name__=='__main__':
    filename = sys.argv[1]
    print(freqs(filename, 2))
