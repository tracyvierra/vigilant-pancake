import numpy as np
import matplotlib.pyplot as plt

data_file = "data.txt"

def sentence_to_array(sentence):
    tokens = sentence.split()
    tokens.append("\n")
    tokens = np.array(tokens)
    return tokens

def array_to_sentence(tokens):
    text = ""
    word_count = 0
    for word in tokens:
        if word in ["THOUGHT", "WORD"]:
            text += word
            word_count += 1
        elif word in ["I", "AM"]:
            text += "I"
        elif word in ["YOU", "VERY", "SO", "WORD"]:
            text += word
        else:
            text += "."
    text = text.strip()
    text = text.split(" ")
    text = ["{}{}".format(token, " ".join(text)) for token in text]
    text = " ".join(text)
    text = text.strip()
    return text

def get_x_and_y(tokens):
    first = tokens[0]
    x = [1 for token in tokens if token == "x"]
    if len(x) == 0:
        y = [0 for token in tokens]
    else:
        x = [0 for token in x]
        y = [0 for token in tokens if token != "x"]
    return x, y

def get_word_count(tokens, text):
    return sum(1 for word in tokens if word in text)

def get_sentence_text(tokens, text):
    return " ".join(get_sentence_text(tokens))

def get_text(tokens):
    """
    Generates a string from the given tokens

    Args:
        tokens: a list of tokens to append to a given text
    Returns:
        text: a string containing all the tokens in tokens appended to a given text
    """
    return tokens + text

def word_from_token_text(text, tokens):
    words = [token for token in text.split() if token in tokens]
    if len(words) == 0:
        return ""
    else:
        return " ".join(words)

def get_text_from_index(index, text, tokens, get_text):
    """
    Generates a string from a given list of tokens.

    Args:
             index: the index of the token to generate the string for
        text: the text in which to generate the string for
        tokens: a list of tokens to append to a given text
        get_text: if True, will be passed the word, else text
    Returns:
        string: a string containing all the tokens in tokens appended to a given text
    """

    return get_text(tokens) + word_from_token_text(text, tokens)

def main():
    sentence = "This is a test sentence."
    tokens = list(word_tokenize(sentence))
    text = list(sentence)
    get_text = True
    get_text_from_index = get_text_from_index
    print(get_text_from_index(0, text, tokens, get_text))

main()
