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
