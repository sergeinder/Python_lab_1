while True:
    try:
        number_of_magic_number = int(input("Input number of magic number: "))
        break
    except ValueError:
        print("You input incorrect data, please try again")

counter = 0
i = 19
while counter != number_of_magic_number:
    i += 9
    my_string = str(i)
    my_sum = 0
    for j in range(len(my_string)):
        my_sum += int(my_string[j])
    if my_sum == 10:
        counter += 1

print(i, counter)
