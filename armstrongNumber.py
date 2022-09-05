#Armstrong Check script
#Written by https://github.com/snmzcm
def main(numberz):
    numberz = 0
    numberCheck = int(numberz)
    digits = len(numberz)
    totalsum = 0
    #print(digits)
    for i in numberz:
        i = int(i)
        sum = i ** digits
        totalsum += sum
        print(f"Digit: {i} ^ {digits} equals to {sum}")
    if totalsum == numberCheck:
        print(f"{numberCheck} is an Armstrong Number ")
    else:
        print(f"{numberCheck} is not an Armstrong Number")





i = 1;
while True:
    main(i)
    i = i + 1;
    if( i == 1000):
        break;