f = open("greeneggs.txt").read()

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    result = {}
    corpus = corpus.split()

    for index,word in enumerate(range(len(corpus) - 2)):
        key = (corpus[index], corpus[index + 1])
        if key in result:
            val.append(corpus[index+1])
        else:
            key = (corpus[index], corpus[index + 1])
            val = [corpus[index + 2]]
        result[key] = val
        
    print result
        

    
make_chains(f)

#PLAN:
#read text
#split text into words
#make a dictionary
#add tuples as keys to dictionary
    #tuple = i + 1
#values are lists of possible words that follow that tuple
