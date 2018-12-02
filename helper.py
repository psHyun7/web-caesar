import string

alphabetL = string.ascii_lowercase
alphabetC = string.ascii_uppercase

def alphabet_position(letter):
    if letter in alphabetL:
        position = alphabetL.index(letter)
        return position
    elif letter in alphabetC:
        position = alphabetC.index(letter)
        return position
    else:
        return letter

def rotate_character(char, rot):
    position = alphabet_position(char)
    if char in alphabetL:
        new_position = (position + rot) % 26
        encrypted = alphabetL[new_position]
        return encrypted
    elif char in alphabetC:
        new_position = (position + rot) % 26
        encrypted = alphabetC[new_position]
        return encrypted
    else:
        return char