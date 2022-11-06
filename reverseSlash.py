def main():
    thePath = str(input("Enter Windows Path: "))
    listPath = list(thePath)
    char =  '\\'
    newlist = ""
    for i, n in enumerate(listPath):
        if n == char:
            listPath[i] = "/"
            newlist = ''.join(listPath)
        
    print(newlist)

    return 0;



main();