"""
To create users in Albridge, a file must be uploaded to their FTP server

Here's a couple of examples of how a Rep File should be formatted

John|Doe|999999999|u99|6|A|||||||

John|Tim|999999999|999999999|1|A||qr|||||

LastName|FirstName|Social|RepID|DataSource|Status|SubCode

"""


def create_user():

    while True:
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
        sub_code = input("Please enter sub code. Leave it blank and hit Enter if no Sub Code for this rep:\n")

        # create rep file and and checks if user is adding a sub rep code
        with open('repfile.txt', 'a') as rep_file:
            rep_file.write(last_name + "|" + first_name + "|" + social + "|" + rep_code + "|" + data_source +
                           "A" + "||")
        # check if sub code is being added. If yes, append the appropriate format to the file.

        if sub_code != ' ':
            with open('repfile.txt', 'a') as rep_file:
                rep_file.write(sub_code + "|||||\n")
        else:
            with open('repfile.txt', 'a') as rep_file:
                rep_file.write("|||||||\n")

        add_another_user_choice = input("Would you like to add another user to this file? Enter Y or N:\n")

        # check if another rep being added
        if add_another_user_choice == "N":
            break


if __name__ == "__main__":
    create_user()






