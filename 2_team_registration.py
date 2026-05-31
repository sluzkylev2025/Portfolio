'''
1) The Online Team Registration Project

● the program requests the name of the team and the number of people in the team
(if the number of students is less than 2 and more than 8, the message “Invalid number of participants” is displayed,
 the program re-requests the name and number of people)
● The program requests the names of the team members based on the specified number
● the account login is made up of the first letters of all participants (the login must be written in lowercase,
the order of names can be any)
● The user needs to come up with a secure password to authorize the team's account, and the program checks its security.
A secure password must consist of at least 8 characters, and there must be no prohibited characters in the password (#%?@/).
If the password does not meet one of the requirements, then one of the messages and the password is requested again:
“The password is too short”
“A forbidden character has been found - *”

● After registration, the team is awarded welcome points:
200 welcome points for each participant.

'''
def name_teem():
    team_name = input('Input team name: ')
    amount_students = int(input('Qty of team persons: '))
    if amount_students < 2 or amount_students > 8:
        print('Impossible qty')
        amount_students = name_teem()
    return amount_students


def names_of_students(amount_students):
    login = ''
    for i in range(amount_students):
        name = input('Input name: ')
        name = name.lower()
        login = login + name[0]
    print('Your login -', login)


def password_team():
    wrong = '#%?@/'
    symbol = '0123456789'
    num = 0
    password = input('Create password: ')
    if len(password) < 8:
        print('Password too short')
        password_team()
    else:
        for s in password:
            if s in wrong:
                print('Impossible symbol found - ', s)
                password_team()


def points(amount_students):
    points_n = amount_students * 200
    print('Your score', points_n, 'points')


amount_students = name_teem()
names_of_students(amount_students)
password_team()
points(amount_students)

