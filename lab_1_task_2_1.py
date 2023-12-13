# Check zero
def end_cycle(my_list):
    for i in range(len(my_list)):
        if my_list[i] != 0:
            return False
    return True


while True:
    my_list = input("Input sequence of numbers: ").split()
    # If string is empty
    while my_list == []:
        my_list = input("Input sequence of numbers: ").split()
    try:
        # Conversion in list of numbers
        my_list = [int(element) for element in my_list]
        break
    except ValueError:
        print("String must contain only numbers")

stepsCounter = 0
while True:
    if end_cycle(my_list):
        break

    minimumObj = max(my_list)
    for i in range(len(my_list)):
        if my_list[i] < minimumObj and my_list[i] != 0:
            minimumObj = my_list[i]

    leftBorder = my_list.index(minimumObj)
    for i in range(leftBorder, 0, -1):
        if my_list[i] != 0:
            leftBorder = i

    rightBorder = my_list.index(minimumObj)
    for i in range(rightBorder, len(my_list)):
        if my_list[i] != 0:
            rightBorder = i

    for i in range(leftBorder, rightBorder + 1):
        my_list[i] -= 1

    stepsCounter += 1

print("Minimum number of steps is", stepsCounter)
