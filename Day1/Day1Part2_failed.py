"""
First digit has lowest index, so we sweep the string backward.
Last digit has highest index, so we sweep the string forward w/ find()
Numerical Texts  = "one", "two", "three",...
Digit = "1", "2", "3",...

Digits and Numerical Texts have their own indices 
=> compare them in the end to update First Digit/Last Digit

about find(): https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_find3
find() return -1 if (substring isn't found or start >= end)
find() finds the first occurrence of matched string.
end by default is len(string) - 1
"""

def NumericalText_Digit(line: str):
    DigitsDict = {
        "one" : 1,
        "two" : 2,
        "three": 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }

    LastNumericalTextIndex = 0
    LastNumericalText = 0

    FirstNumericalTextIndex = len(line)
    FirstNumericalText = 0

    for key, _ in DigitsDict.items():
        
        # find 1st occurance of keyword in line
        occuranceIndex = line.find(key) 
        if occuranceIndex != -1:
            if occuranceIndex < FirstNumericalTextIndex:
                FirstNumericalText = DigitsDict[key]
                FirstNumericalTextIndex = occuranceIndex

            # Find other instances of  LastNumericalText 
            while True:
                if occuranceIndex > LastNumericalTextIndex:
                    LastNumericalText = DigitsDict[key]
                    LastNumericalTextIndex = occuranceIndex
                occuranceIndex = line.find(key, occuranceIndex + len(key)) 
                
                # if no occurance afterward, find() return -1 so break loop
                if occuranceIndex == -1:
                    break

    ### Find digit string
    digits = list(filter(lambda x: x.isdigit(), [*line]))
    if digits: # if list digit isn't empty
        FirstDigit = int(digits[0])
        FirstDigitIndex =  line.find(digits[0])
        if FirstNumericalTextIndex < FirstDigitIndex:
            FirstDigit = FirstNumericalText

        LastDigit = int(digits[-1])
        LastDigitIndex = line.find(digits[-1])
        if LastNumericalTextIndex > LastDigitIndex:
            LastDigit = LastNumericalText
    
    else: #if it is
        FirstDigit = FirstNumericalText
        LastDigit = LastNumericalText

    return (FirstDigit*10 + LastDigit)

line = "oneightwoneight"
line = "7onetwozrl7fbxhqgrbtoneightpzv"
line = "kjvoneighteightfivepsbkgdgpndxx7six8"
line = "ndoneight361"
line = "fiveseven1czvlmlncthreerstssbjdoneightpm"
line = "1nineoneightxqt"
line = "eight8sevenoneightjtj"
line = "threesix2oneoneightc"
line = "rkllqvfjz13sixthreetdztlhlcldoneightj"
line = "honeighttpqxdbhsevengvzfourd4s5"
line = "7onetwozrl7fbxhqgrbtoneightpzv"
line = "tjoneightone9three9dkbnh"
line = "eightbpsqrkzhqbhjlrxmzsixvvmgtrseventwo7oneightjbx"
line = "99sixv"
line = "gdoneight26pzghbjfeightttfbvhltwo8"
print(NumericalText_Digit(line))
