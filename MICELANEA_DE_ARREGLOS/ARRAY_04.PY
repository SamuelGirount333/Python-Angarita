array =  [17, 4, 64, 79, 109, 112]

for item in array:
    if item:
        solved = item % 2
        if solved == 0:
            print(item)
