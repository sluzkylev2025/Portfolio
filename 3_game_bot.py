'''This is a bot for a book club. What can a bot do?
● Registers users by requesting their name and interests (registration is required)
● offers a choice of actions in the main menu (1-Find a friend 2- Play 3- Exit), after each action you can return to the main menu
● searches for friends based on the user's interests (% matches are more than 15), prints the interests of a friend who did not match
● Launches 3 games (Scrabble, Unique Symbols, Anagrams) The winning and losing conditions can be changed

The program already stores a database with the interests of 5 users in a dictionary format, in which the keys are user numbers from 1 to 5, the value is a list of the user's name and a set with his interests. Each user has 4 interests.
Copy the dictionary: people = {1: ['Ivan', {'fiction','comics','detective', 'novel'}], 2: ['Marina', {'comics', 'fantasy', 'detective', 'comedy'}], 3: ['Tim', {'fiction', 'horror', 'detective', 'drama'}], 4: ['Nikita', {'fantasy', 'comedy', 'mystery', 'comic'}], 5: ['Vladimir', {'comic', 'romance', 'comedy', 'drama'}]}

We have prepared a detailed description of each stage of the project creation, use it to explain.

1) Registration
The program requests the user's name and interests. Interests need to be recorded in a set.
Students can add or not add data to the dictionary (this is not in the TOR, so it is at the discretion of the student

2) Find a friend

● if the user's interests match 1 of the 5 specified people by more than 15%, then the name of the recommended friend and the % match with him are displayed. There may be several proposed friends
● For each friend, the bot outputs interests that do not match


3) The game “Scrabble”

In the Scrabble board game, each letter has a certain value. Russian letters are evaluated as follows:
● A, B, E, I, N, O, R, S, T – 1 point;
● D, K, L, M, P, Y – 2 points;
● B, D, E, B, I – 3 points;
● Y, Y – 4 points;
● W, W, X, C, H – 5 points;
● W, E, Y – 8 points;
● F, Sch, B – 10 points.

Write a function that calculates the cost of a user-entered word. Hint: use a dictionary. Important: the user has only 1 word, which contains only Russian letters.

In this game, we did not add a win and loss condition. Students can do this. For example, a word with more than 18 points leads to a victory.

4) The Unique Letters Game
The user enters a word or string, and the program calculates how many unique characters are contained (without duplicates).
For example, banana - 3; symbol - 6
The goal: to come up with a sentence with more than 15 unique characters.
The winning and losing conditions can be changed

5) The Anagram Game

An anagram is a rearrangement of letters in a word to make a new word. For example, growth - grade - cable

Write a function that asks for 3 words. If the words are anagrams, then the message “Super” is displayed, otherwise “Don't try to cheat.”
Hint: Choose the data type to store each letter of the word and the number of its repetitions.
The winning and losing conditions can be changed'''

people = {1: ['Ivan', {'fiction','comics','detective', 'novel'}],
          2: ['Marina', {'comics', 'fantasy', 'detective', 'comedy'}],
          3: ['Tim', {'fiction', 'horror', 'detective', 'drama'}],
          4: ['Nikita', {'fantasy', 'comedy', 'drama', 'comic'}],
          5: ['Vladimir', {'comic', 'novel', 'comedy', 'drama'}]}


def reg():
    name = input("Input your name ")
    a = input('Enter 4 book genres separated by a space: fiction, detective, comedy, novel, comic, fantasy, drama, etc.').split()
    a = set(a)
    return a


def find_friend(a):
    for i in (people):
        result1 = a & (set(people[i][1]))
        result2 = a.union((set(people[i][1])))
        result = len(result1) / len(result2) * 100
        if round(result) > 15:
            print(people[i][0], round(result))
            print(people[i][1] - a)
    start()


def scrubble():
    points_ru = {1: 'AEIONRTLSU',
                 2: 'DG',
                 3: 'BCMP',
                 4: 'FHVWY',
                 5: 'K',
                 8: 'JX',
                 10: 'QZ'}
    text = input().upper()
    print(sum([k for i in text for k, v in points_ru.items() if i in v]))
    a = input('1-Start game again 2-Main мenu')
    if a == '1':
        scrubble()
    elif a == '2':
        start()


def unic():
    n = set(input().lower())
    if len(n) > 15:
        print('Win')
    else:
        print('You need', 16 - (len(n)))
    a = input('1-Start game again 2-Main мenu')
    if a == '1':
        unic()
    elif a == '2':
        start()


def anagram():
    a, b, c = input(), input(), input()
    a = {i: a.count(i) for i in a}
    b = {i: b.count(i) for i in b}
    c = {i: c.count(i) for i in c}
    print('Super' if a == b== c else "Don't try to cheat")
    a = input('1-Start game again 2-Main мenu')
    if a == '1':
        anagram()
    elif a == '2':
        menyuishka()


def start():
    action = input('1-find a friend 2-Play 3-Exit')
    if action == '1':
        find_friend(a)
    if action == '2':
        game = input('1-Scrabble 2-Unique letters 3-Anagrams')
        if game == '1':
            scrubble()
        elif game == '2':
            unic()
        elif game == '3':
            anagram()
    if action == '3':
        print('Bye')


a = reg()
start()

