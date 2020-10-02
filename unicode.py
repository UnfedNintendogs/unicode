import subprocess


def list():
    with open("characters.txt") as f:
        for line in f:
            print(line, end='')


def encode():
    letter = int(input('Number? '))
    number = chr(letter)
    print(number)
    temp = number
    number = letter
    letter = temp
    writetext(number, letter)


def writetext(number, letter):
    f = open("characters.txt", "a+")
    words = str(number) + " = " + str(letter)
    f.write(words)
    subprocess.Popen(
        ['sort characters.txt -n -b -u -o characters.txt'], shell=True)
    f.close()


def decode():
    letter = input('Letter? ')
    number = ord(letter)
    print(number)
    writetext(number, letter)


def questions():

    boi = input("Encode, Decode or List: ")

    if boi == "encode" or boi == "Encode":
        encode()

    elif boi == "decode" or boi == "Decode":
        decode()

    elif boi == "list" or boi == "List":
        list()

    else:
        print("Invalid Input")
        questions()


questions()
