
def palin(word):
    def make_palin_right(word,i,letters):
        if i >= len(word) :
            return letters
        if word[len(word)-i-1] != (''.join(letters)+word)[i]:
            return make_palin_right(word,i+1,letters+[word[len(word)-i-1]])
        return make_palin_right(word,i+1,letters)
    def interleve_palin(word,i,letters):
        if i >= len(word)/2:
            return letters
        if word[i] != (word[len(word)-i-1]):
            return interleve_palin(word[0:len(word)-i]+word[i]+word[len(word)-i:],i+1,letters+[word[i]])
        return interleve_palin(word,i+1,letters)
    right=make_palin_right(word,0,[])
    left=interleve_palin(word,0,[])
    return (len(right)<=len(left) and right) or left

if __name__ == "__main__":
    print(palin("casa"))
    print(palin("otto"))
    print(palin("palindromo"))
    print(palin("posero"))
    print(palin("coccinella"))
