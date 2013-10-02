#!/usr/bin/env python

from sys import argv
import random
import twitter


def twitter_push(message):
    api = twitter.Api()
    status = api.PostUpdate(message)
    print status.text



def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""
    markov_dictionary = {}
    corpus = corpus.split()

    for index in xrange(len(corpus) - 2):
        key = (corpus[index], corpus[index + 1])
        val = corpus[index + 2]
        if key not in markov_dictionary:
            markov_dictionary[key] = [val]
        else:
            #longhand version:
            # mk_list = markov_dictionary[key]
            # mk_list.append(val)
            # markov_dictionary[key] = mk_list
            markov_dictionary[key].append(val)       
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
    first_key = random.choice(chains.keys())
    first_value = random.choice(chains[first_key])
    tweet_content.append(first_key[0])
    tweet_content.append(first_key[1])
    tweet_content.append(first_value)
    new_key_index = 1
    while len(" ".join(tweet_content)) <= 120:
        current_key = tweet_content[new_key_index], tweet_content[new_key_index + 1]
        current_value = random.choice(chains[current_key])
        tweet_content.append(current_value)
        new_key_index += 1

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
    script, inputfile = argv
    input_text = open(inputfile).read()
    chain_dict = make_chains(input_text)
    random_text = make_text(chain_dict)
    twitter_push(random_text)


if __name__ == "__main__":
    main()

