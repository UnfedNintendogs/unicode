import subprocess


def list():
    with open("characters.txt") as f:
        for line in f:
            print(line, end='')
    quit()


def encode():
    letter = int(input('Number? '))
    number = chr(letter)
    print(number)
    temp = number
    number = letter
    letter = temp
    writetext(number, letter)
    quit()


def writetext(number, letter):
    f = open("characters.txt", "a+")
    words = str(number) + " = " + str(letter) + "\n"
    f.write(words)
    f.seek(0)
    linesinfile = f.readlines()
    lines = sorted(linesinfile, key=lambda line: int(line.split()[0]))
    finallines = dict.fromkeys(lines)
    f.truncate(0)
    for line in finallines:
        f.write(line)
    f.close()


def decode():
    letter = input('Letter? ')
    number = ord(letter)
    print(number)
    writetext(number, letter)
    quit()


def questions():

    type = input("Encode, Decode or List: ")

    if type == "encode" or type == "Encode":
        encode()

    elif type == "decode" or type == "Decode":
        decode()

    elif type == "list" or type == "List":
        list()

    else:
        print("Invalid Input")
        questions()


questions()
