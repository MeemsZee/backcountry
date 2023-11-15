user_input = input("Enter expression: ").strip().split()
first_number = int(user_input[0])
math_operator = user_input[1]
second_number = int(user_input[2])

match math_operator:
    case "+":
        print(float(first_number + second_number))
    case "-" :
        print(float(first_number - second_number))
    case "*" :
        print(float(first_number * second_number))
    case "/" :
        print(float(first_number / second_number))