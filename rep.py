class User:
    def __init__(self, last_name, first_name, social, rep_code, data_source):
        self.last_name = last_name
        self.first_name = first_name
        self.social = social
        self.rep_code = rep_code
        self.data_source = data_source


def create_user():

    # prompt for user info and write to file
    last_name = input("Please enter user last name:\n")
    first_name = input("Please enter user first name:\n")
    social = input(str("Please enter user social security number:\n"))

    # test if social is a digit
    while not social.isdigit():
        social = input("That's an invalid Social. Please re-enter the social security number:\n")
        if social.isdigit():
            break

    # continue asking for input
    rep_code = input("Please enter user rep code:\n")
    data_source = input("Please choose the Data Source. Enter 6 for NFS, 1 for DST, 2 for DAZL:\n")
    sub_code_check = input("Are you adding an adviser sub code? "
                           "Type \"Y\" for yes and \"N\" for no and hit Enter:\n")

    # run if user is adding sub code
    if sub_code_check == "Y":
        sub_code = input("Please enter sub code:\n")

    user = User(last_name, first_name, social, rep_code, data_source)
    print(user.social)

    add_another_user_choice = input("Would you like to create add another user to this file?:\n")

    if add_another_user_choice == "davi":
        print(add_another_user_choice)


if __name__ == "__main__":
    create_user()






