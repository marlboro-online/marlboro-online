while True:

    print("welcome to maths automatic v1!")
    operation = input("what operation would you like? + for addition, - for subtraction, x for multiplication and / for division ")

    operation = operation.strip( )

    if operation == "+":
        print("you chose addition")

    elif operation == "-":
        print("you chose substration")

    elif operation == "x":
        print("you chose multiplication")

    elif operation == "/":
        print("you chose division")

    else:
        print("you didn't pick anything! try again")

    first_number = input("First digit:")
    second_number = input("Second digit:")
    if operation == "+":
        sum = float(first_number) + float(second_number)

    elif operation == "-":
        sum = float(first_number) - float(second_number)

    elif operation == "x":
        sum = float(first_number) * float(second_number)

    elif operation == "/":
            sum = float(first_number) / float(second_number)

    else:
         print("try again")

    print("the answer is " + str(sum) +"!")

    x = input("go again? Y for yes N for no ").upper()
    if x == "Y":
        continue

    else:
        print("thanks for using maths automatic v1! :) ")
        break