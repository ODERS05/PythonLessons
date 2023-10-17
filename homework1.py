fname = input("Enter file name : ")
try:
    if fname != "writefile.txt":
        raise NameError
    else:
        fhand = open(fname, "r")
        line = fhand.read()
        print(line.upper())
        fhand.close()
except NameError:
    print("File with this name doesn't exist!")