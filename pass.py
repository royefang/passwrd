#!/usr/bin/env python3
import string, random

print('Choose between a randomly generated password (1) or hashing a memorable phrase (2).')
choice = int(input())

#random password
if choice == 1:
    alphaList = list(string.ascii_letters)
    digitList = list(string.digits)
    punctList = list(string.punctuation)

    print("Enter desired length of password (between 3 and 50).")
    len = int(input())

    result = ''
    x = 0

    #invalid password amount
    if len > 50 or len < 3:
        raise Exception('Invalid length. Please enter a length between 3 and 50')
    
    #if len is 3, generate password with one letter, digit, and special character
    elif len == 3:
        tempList = [random.choice(alphaList),
                random.choice(digitList),
                random.choice(punctList)]    
        random.shuffle(tempList)
        result = result.join(tempList)

    #length between 3 and 7
    elif len < 8:
        result += random.choice(alphaList)
        result += random.choice(punctList)
        while(x < len-3):
            tempCase = random.randint(0,2)
            if tempCase == 0:
                result += random.choice(alphaList)
            elif tempCase == 1:
                result += random.choice(digitList)
            else:
                result += random.choice(punctList)
            x += 1
            result += random.choice(digitList)

    #length between 8 and 50
    else:
        while(x < len):
            tempCase = random.randint(0,2)
            if tempCase == 0:
                result += random.choice(alphaList)
            elif tempCase == 1:
                result += random.choice(digitList)
            else:
                result += random.choice(punctList)
            x += 1

    print(result)

#hashing a memorable phrase
elif choice == 2:

    print("Enter a memorable phrase (for example: The quick brown fox jumps over the lazy dog")
    tempStr = input()

    print("Enter some special characters (for example: !@#")
    tempSpecial = input()

    print("Enter some digits: for example: 23748")
    tempDigits = input()

    inputList = str(tempStr).split()
    specialList = str(tempSpecial)
    digitStr = str(tempDigits)
    digitList = digitStr.split()

    result = ''
    for x in inputList:
        tempCase = random.randint(0,1)
        if tempCase == 0:
            result += x[0].upper()
        else:
            result += x[0].lower()
        
    #result is now a string that contains randomly capitalized letters

    tempCaseDigits = random.randint(0,1)

    #randomly distribute nums
    if tempCaseDigits == 0:

        for x in digitList:
            tempCase = random.randint(0,1)
            if tempCase == 0:
                result = x + result
            else:
                result += x

    #else slap some numbers on the front or end of string
    else:
        tempCase = random.randint(0,1)
        if tempCase == 0:
            result = digitStr + result
        else:
            result += digitStr

    for x in specialList:
        tempCase = random.randint(0,1)
        if tempCase == 0:
            result = x + result
        else:
            result += x

    #result now contains randomly placed letters, numbers, and 
    #characters based on a given phrase
    print(result)

# :(
else:
    raise Exception('Invalid choice. Please enter (1) or (2)')