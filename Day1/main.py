file1 = open('calibrationIn.txt', 'r')
Lines = file1.readlines()

totalCalibration = 0
for line in Lines:
    totalCalibration = totalCalibration + NumericalText_Digit(line)
print(totalCalibration)
