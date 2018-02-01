import string, sys, itertools

if len(sys.argv)>=2:
    dictionary_length = int(sys.argv[1])
else:
    dictionary_length = 3

if len(sys.argv)>=3:
    filename = sys.argv[2]
else:
    filename = "dictionary.txt"

ascii_chars = string.ascii_letters+string.digits
ascii_len = len(ascii_chars)

def generate_dic():
    charList = []
    for char in ascii_chars:
        charList.append(char)
    return charList

def write(char):
        fileStream.write(char+" ")

def main():
    for i in range(dictionary_length):
        args = (i+1)*[generate_dic()]
        for combination in itertools.product(*args):
            printable = ""
            for element in combination:
                printable+=element
            write(printable)

if __name__=="__main__":
    fileStream = open(filename,"w")
    main()
    fileStream.close()
