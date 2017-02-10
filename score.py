import os


def decode(string, shift):
    decoded = ""
    for symbol in string:
        number = ord(symbol) + shift
        decoded += chr(number)
    return decoded

def encode(string, shift):
    encoded = ""
    for symbol in string:
        number = ord(symbol) - shift
        encoded += chr(number)
    return encoded

def read_score():
    scores = []
    try:
        with open("score.bin", "x") as f:
            pass
    except:
        pass
    with open("score.bin", "r") as f:
        for line in f:
            decoded = decode(line[:-1], 5).split()
            if decoded:
                try:
                    scores.append((decoded[0], int(decoded[1])))
                except:
                    pass
    
    scores.sort(key=lambda tup: int(tup[1]), reverse=True)
    return scores

def save_score(name, score):
    scores = read_score()
    if len(scores)==10:
        if scores[-1][1] < score:   
            del scores[-1]
            scores.append((name, score))
        else:
            return
    else:
        scores.append((name, score))

    with open("score.bin", "w") as f:
        for line in scores:
            data = str(line[0]) + str(" ") + str(line[1])
            f.write(encode(data, 5)+"\n")