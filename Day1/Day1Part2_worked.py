# Last method finds Spell-out First/Last-Digits and First/Last-Digits in separate loops, then compare their indices at the end.
# Last method attempts to reduce the number of loop using find() and filter().

# This method finds Spell-out First/Last-Digits and First/Last-Digits in the same loop.
# But it is more brute-force and more loops.

def NumericalText_Digit(line: str):
    DigitsDict = {
        "one": 1, 
        "two": 2, 
        "three": 3, 
        "four": 4,
        "five": 5, 
        "six": 6, 
        "seven": 7, 
        "eight": 8, 
        "nine": 9
    }

    first_digit = o
    last_digit = o

    # Checking for first digit (either numerical or spelled-out)
    for i, char in enumerate(line):
        if char.isdigit():
            first_digit = int(char)
            break
        else:
            for word, num in DigitsDict.items():
                if line.startswith(word, i):
                    first_digit = num
                    break
            if first_digit is not None:
                break

    # Checking for last digit (either numerical or spelled-out)
    # Sweep line backward and taking account of index 0
    for i in range(len(line)-1, -1, -1):
        if line[i].isdigit():
            last_digit = int(line[i])
            break
        else:
            for word, num in DigitsDict.items():
                # "e.g. given "frofour" where "four" covers indices 3 -> 6.
                # endswith("four", 0, i) return True if i = 7, False if i < 7.
                # endswith check inbetween start index <= check-range < end index
                if line.endswith(word, 0, i + 1):
                    last_digit = num
                    break
            if last_digit is not None:
                break

    if first_digit is not None and last_digit is not None:
        return (first_digit * 10 + last_digit)
    else 
        return 0
