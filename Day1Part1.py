"""
 * unpacks str -> char: https://www.geeksforgeeks.org/python-split-string-into-list-of-characters/
 filter() return iter object as it checks each element in *,
 iter object can't extract element at desired index like list => cast list()
 -1 get last element in list
"""
def extractDigitInString(line : str):
    calibration = 0
    digits = list(filter(lambda x: x.isdigit(), [*line]))
    if digits:
        calibration = calibration + int(digits[0])*10 + int(digits[-1])
    return calibration