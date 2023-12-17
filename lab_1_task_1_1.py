def correct_input(result_str):
    while result_str.replace(" ", "") == "":
        print("You entered an empty string")
        result_str = input("Try again: ")
    return result_str


written_string = input("Input your string: ")
written_string = correct_input(written_string)

virus = input("Input your virus: ")
virus = correct_input(virus)

lower_virus = virus.lower()

# We use binary representation of a number as sequence of upper and lower letter
# I know it is so hard, but I don't see another way
for i in range(0, 2 ** (len(virus))):
    # writing the code
    code = str(bin(i))[2:]
    if len(code) < len(virus):
        code = "0" * (len(virus) - len(code)) + code

    # reading the code
    new_virus = ""
    for j in range(len(code)):
        if code[j] == "1":
            new_virus += lower_virus[j].upper()
        else:
            new_virus += lower_virus[j]

    written_string = written_string.replace(new_virus, "")
print("Result string: ", written_string)
