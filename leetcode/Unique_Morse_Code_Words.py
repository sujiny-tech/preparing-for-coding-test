words=["gin", "zen", "gig", "msg"]

def uniqueMorseRepresentations(words):
    #full table for the 26 letters of the English alphabet
    letters=[".-","-...","-.-.","-..",".","..-.",
             "--.","....","..",".---","-.-",".-..",
             "--","-.","---",".--.","--.-",".-.","...",
             "-","..-","...-",".--","-..-","-.--","--.."]

    #transformations of words
    all_=[]
    
    for word in words:
        mid=""
        for i in range(len(word)):
            mid+=letters[ord(word[i])-97]
    
        if mid not in all_:
            all_.append(mid)
    return len(all_)

print(uniqueMorseRepresentations(words))
