def correct_data():
    while True:
        while True:
            try:
                this_list = [int(j) for j in input("Enter the row number, seats and cost: ").split()]
                break
            except ValueError:
                print("You input incorrect data, please enter the row number, seats and cost")
        flag = True
        if len(this_list) == 3:
            for i in range(3):
                if this_list[i] < 1:
                    print("You input incorrect data, please enter the row number, seats and cost")
                    flag = False
        else:
            flag = False
        if flag:
            return this_list


# Input number of string
while True:
    try:
        number_of_string = int(input("Input your number: "))
        if number_of_string < 1:
            raise ValueError()
        break
    except ValueError:
        print("You input incorrect data, please input number")

my_dict = {}
for i in range(number_of_string):
    # Input the row number, seats and cost
    my_list = correct_data()
    row_ans_seat = (my_list[0], my_list[1])
    if row_ans_seat in my_dict:
        my_dict[row_ans_seat].add(my_list[-1])  # Add cost
    else:
        my_dict[row_ans_seat] = {my_list[-1]}

for i in my_dict:
    print(str(i)[1:-1].replace(",", ""), "-", len(my_dict[i]), sep=" ")
