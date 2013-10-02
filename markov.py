#!/usr/bin/env python

from sys import argv
script, inputfile = argv
import random


def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_dictionary = {}
    corpus = corpus.split()

    for index in xrange(len(corpus) - 2):
        key = (corpus[index], corpus[index + 1])
        if key not in markov_dictionary:
            val = [corpus[index + 2]]
            markov_dictionary[key] = val
        else:
            #longhand version:
            # mk_list = markov_dictionary[key]
            # mk_list.append(val)
            # markov_dictionary[key] = mk_list

            #shorthand version:
            markov_dictionary[key].append(corpus[index+1])       
    return markov_dictionary
        
def change_tuple(tupl):
    lista = []
    lista.append(tupl[0])
    lista.append(tupl[1])
    return lista

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    tweet_content = []
    while len(" ".join(tweet_content)) <= 120:
        tweet_key = random.choice(chains.keys())
        tweet_value = random.choice(chains[tweet_key])
        tweet_key = change_tuple(tweet_key)
        tweet_content.append(tweet_key[0])
        tweet_content.append(tweet_key[1])
        tweet_content.append(tweet_value)

    while len(" ".join(tweet_content)) >= 30:
        if "!" in tweet_content[-1]:
            break
        elif "." in tweet_content[-1]:
            break
        elif "?" in tweet_content[-1]:
            break
        else:
            del tweet_content[-1]

    if len(" ".join(tweet_content)) < 30:
        return  " ".join(tweet_content) + "...!"
        #return " ".join(tweet_content)[0].upper() + " ".join(tweet_content[1:-1] + "...!"
    else:
        return " ".join(tweet_content)



def main():
    #args = sys.argv

    # Change this to read input_text from a file
    input_text = open(inputfile).read()

    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    print random_text

if __name__ == "__main__":
    main()

