import random

def generate_key():
    key = ''
    key_len = 50
    spec_char = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '<', '>', '?', '/']
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    alphabet_upper = []
    for i in range(len(alphabet)):
        alphabet_upper.append(alphabet[i].upper())

    for j in range(key_len):
        switch = random.randint(1, 4)
        if switch == 1:
            key += spec_char[random.randint(0, 11)] 
        elif switch == 2:
            key += alphabet[random.randint(0, 25)]
        elif switch == 3:
            key += alphabet_upper[random.randint(0, 25)]
        elif switch == 4:
            key += str(random.randint(0, 9))
    return key