tup = ((2,5),(4,2),(9,8),(12,10))
count = 0
tup_length = len(tup)
for  i in range (tup_length):
    if tup [i][0] % 2 == 0 and tup[i][1] % 2 == 0:
        count = count + 1
print("The number of pair where both a and b are even:", count)