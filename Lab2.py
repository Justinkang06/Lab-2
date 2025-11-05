def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    # 1. Read numbers entered by the user
    user_input = input()

    # 2. Split the string into a list of strings using ',' as separator
    str_list = user_input.split(',')

    float_list = []

    print(str_list)

    for string in str_list:
        float_num = float(string)
        float_list.append(float_num)
    return float_list

    # 3. Convert the list of strings to a list of floats
    # float_list = [float(num) for num in str_list]

    # 4. Return the list of floats
    return float_list


def main():
    print("ET0735 (DevOps for AIoT) - Lab2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)


if _name_ == "_main_":
    main()