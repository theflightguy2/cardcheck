def validitycheck(cardnum:str):
    if len(cardnum) > 16:
        print("Too Long")
        return False
    elif len(cardnum) < 16:
        print("Too short")
        return False
    else:
        print("Correct Length")
        try:
            int(cardnum)
        except:
            print("CARD NUMBER MUST JUST BE LETTERS")
            return False
        else:
            return True


cardnum = input("Enter Card Number: ")

while validitycheck(cardnum) != True:
    cardnum = input("Enter Card Number: ")

pan = cardnum[6:15]
checksum = cardnum[-1]

def issuercheck(cardnum):
    leading2 = cardnum[0:2]
    if leading2[0] == "4":
        return "VISA"
    elif leading2 == "34" or leading2 == "37":
        return "AMEX"
    elif int(leading2) in range(51, 56):
        return "MASTERCARD"
    elif leading2[0] == "4":
        return "JCB"
    else:
        return -1

while issuercheck(cardnum) == -1:
    print("Invalid issuer")
    cardnum = input("Enter Card Number: ")

issueresult = issuercheck(cardnum)

def checkLuhn(cardNo):
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False

    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')

        if (isSecond == True):
            d = d * 2

        # We add two digits to handle
        # cases that make two digits after
        # doubling
        nSum += d // 10
        nSum += d % 10

        isSecond = not isSecond

    if (nSum % 10 == 0):
        return True
    else:
        return False

if checkLuhn(cardnum):
    print("Card is Valid")
    print(f"Issuer is {issueresult}")
else:
    print("Card is Invalid - Issuer Type False")

