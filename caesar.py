from helpers import alphabet_position, rotate_character

def rotate_string(text, rot):
    encrypted = ""
    for char in text:
        newchar = rotate_character(char, rot)
        encrypted += newchar
    return encrypted

def main():
    message = input("Type a message:")
    rotation = int(input("Rotate by:"))
    print(rotate_string(message, rotation))

if __name__ == "__main__":
    main()
