def main():
    thePath = str(input("Enter Windows Path: "))
    listPath = list(thePath)
    char =  '\\'
    char2 = ':'
    newlist = ""
    for i, n in enumerate(listPath):
        if n == char:
            listPath[i] = "/"
            newlist = ''.join(listPath)
        elif n == char2:
            listPath[i] = ""
            newlist = ''.join(listPath)

        
    print("" + "/mnt/" + newlist.lower())

    return 0;



main();