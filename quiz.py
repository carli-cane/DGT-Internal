"""This is a multi choice quiz giving users the choice of 6 subjects."""
import easygui
TITLE = "Carli's Quiz"
MIN_AGE = 14
MAX_AGE = 18
NUM_QNS = 5
score = 0   # how many they get right
answers = 0  # how many they've answered

# The different subjects the user can chose from
SUBJECTS = ["Science", "Math", "History", "Geography", "Riddles", "General"]
# Five questions per subject so that user can do any of the six subjects
Q_SCIENCE = ["What is the center of an atom called?", "What gas makes up most of our atomsphere?", "Which is the correct formula for speed?", "How many chambers does the human heart have?", "How many elements are on the periodic table?"]
Q_MATH = ["What is the name of this formula 'A^2 + B^2 = C^2'", "How many degress is a right angle?", "What is the highest common factor (HCF) of 60 and 40?", "What is 16 x 4?", "If x + 10 = 28 what is the value of x?"]
Q_HISTORY = ["What year did World War 2 start?", "What day is a memorial day for soldiers in New Zealand and Australia?", "How many years did the 100 year war last?", "What year did Hitler commit suicide?", "Who was the first person on the moon?"]
Q_GEO = ["What is the capital of the United States?", "Which gulf recently had its name changed?", "What country is the Leaning Tower of Pisa in?", "Which country has a replica of the Statue of Liberty?", "What country is closest to Greenland?"]
Q_RIDDLES = ["What is full of holes but still holds water?", "The more there is, the less you see. What is it?", "What has many keys but cannot open any doors?", "Where does today come before yesterday?", "What has lots of eyes but cannot see?"]
Q_GENERAL = ["What is a group of crows called?", "How many hearts does an octopus have?", "What is the rarest blood type?", "Who is the greek god/goddess of love?", "What is the only planet that rotates on its side?"]

# Correct answers for each question inside each. subject
CA_SCIENCE = ["Nucleus", "Nitrogen", "Distance/Time", "4", "118"]
CA_MATH = ["Pythagoras Theorum", "90", "20", "64", "18"]
CA_HISTORY = ["1939", "ANZAC day", "116", "1945", "Neil Armstrong"]
CA_GEO = ["Washington D.C", "Gulf of Mexico", "Italy", "France", "Canada"]
CA_RIDDLES = ["Sponge", "Darkness", "Piano", "The dictionary", "A potato"]
CA_GENERAL = ["Murder", "3", "-AB", "Aphrodite", "Uranus"]

# Four answers per question for each subject
A_SCIENCE = [["Middle", "Nucleus", "Centre", "Heart"], ["Carbon Dioxide", "Nitrogen", "Oxygen", "Carbon"], ["Distance/Time", "Time/Distance", "Speed/Time", "Distance/Speed"], ["2", "1", "4", "5"], ["112", "100", "118", "200"]]
A_MATH = [["Triangle Formula", "Quadratic Equation", "Pythagoras Theorum", "Law of Gravity"], ["180", "100", "80", "90"], ["6", "4", "12", "20"], ["32", "68", "44", "64"], ["12", "16", "20", "18"]]
A_HISTORY = [["1940", "1921", "1948", "1939"], ["ANZAC day", "Memorial day", "Remembrance day", "Victory day"], ["50", "100", "116", "101"], ["1942", "1946", "1945", "1940"], ["Neil Armstrong", "John Glenn", "Buzz Aldrin", "Alan Shepard"]]
A_GEO = [["New York", "Washington D.C", "Chicago", "Canada"], ["Gulf of America", "Gulf of Panama", "Gulf of Mexico", "Gulf of Oman"], ["France", "Italy", "America", "Romania"], ["None", "Brazil", "France", "United Kingdom"], ["Iceland", "America", "Canada", "Denmark"]]
A_RIDDLES = [["Sponge", "Bucket", "Mouth", "Wells"], ["Light", "Darkness", "Air", "Speed"], ["Key ring", "Piano", "Fish", "Doors"], ["Never", "The dictionary", "In the future", "In the past"], ["Missisipi", "A blind person", "A potato", "A key"]]
A_GENERAL = [["Flock", "Group", "Murder", "Fowl"], ["2", "1", "12", "3"], ["O+", "-AB", "-O", "AB"], ["Ares", "Demeter", "Persephone", "Aphrodite"], ["Neptune", "Uranus", "Jupiter", "Earth"]]

easygui.msgbox("Welcome to the game", TITLE)
easygui.msgbox("This quiz is designed for people aged 15 to 18")
age = easygui.integerbox("So before we begin, how old are you?", TITLE)
# if the user is in the allocated age range
if age > MIN_AGE and age < MAX_AGE:  
    easygui.msgbox("You are old enough to play", TITLE)
    name = easygui.enterbox("What is your name?", TITLE)
    easygui.msgbox("Welcome " + name, TITLE)
    easygui.msgbox("This quiz will have 5 multiple choice questions and when we begin you will have your choice between 6 subjects")
PLAY_AGAIN = "Yes"
# makes sure to only play the quiz while the age is in the correct range
while PLAY_AGAIN == "Yes" and age > MIN_AGE and age < MAX_AGE:  
    while answers < NUM_QNS:
        subject = easygui.buttonbox("What would you like to be quizzed on?", TITLE,  SUBJECTS)
         # removes the subject the user chose so they can't do it again if they choose to play again
        for x in SUBJECTS[:]: 
            if x == subject:
                SUBJECTS.remove(x)

        def quiz(subject, question, ca_answer, answer):  # my main structure for my quiz
            """This function runs the entirety of the quiz."""
            score = 0    # how many they get right
            answers = 0   # how many they've answered
            # runs the quiz till user has answered 5 questions
            while answers < NUM_QNS:  
                easygui.msgbox("Awesome! You will be answering " + subject + " questions", TITLE)
                # first attempt at question
                choice = easygui.buttonbox(question[0], TITLE, choices=answer[0])  
                # if the first attempt is wrong
                if choice != ca_answer[0]:
                    easygui.msgbox("Sorry that was incorrect. Try again", TITLE)
                    # second attempt at question
                    choice2 = easygui.buttonbox(question[0], TITLE, choices=answer[0])  
                    # if the second attempt is wrong
                    if choice2 != ca_answer[0]:
                        easygui.msgbox("Sorry that was incorrect", TITLE)
                        easygui.msgbox("The answer was " + ca_answer[0], TITLE)
                        answers += 1
                    # if the second attempt is correct
                    if choice2 == ca_answer[0]:
                        easygui.msgbox("That was correct!", TITLE)
                        answers += 1
                # if the first attempt is correct
                if choice == ca_answer[0]:
                    easygui.msgbox("Well done! That was correct", TITLE)
                    answers += 1
                    score += 1
                # first attempt at question
                choice = easygui.buttonbox(question[1], TITLE, choices=answer[1])
                if choice != ca_answer[1]:
                    easygui.msgbox("Sorry that was incorrect. Try again", TITLE)
                    # second attempt at question
                    choice2 = easygui.buttonbox(question[1], TITLE, choices=answer[1])
                    if choice2 != ca_answer[1]:
                        easygui.msgbox("Sorry that was incorrect", TITLE)
                        easygui.msgbox("The answer was " + ca_answer[1], TITLE)
                        answers += 1
                    if choice2 == ca_answer[1]:
                        easygui.msgbox("That was correct!", TITLE)
                        answers += 1
                if choice == ca_answer[1]:
                    easygui.msgbox("Well done! That was correct", TITLE)
                    answers += 1
                    score += 1
                # first attempt at question
                choice = easygui.buttonbox(question[2], TITLE, choices=answer[2])
                if choice != ca_answer[2]:
                    easygui.msgbox("Sorry that was incorrect. Try again", TITLE)
                    # second attempt at question
                    choice2 = easygui.buttonbox(question[2], TITLE, choices=answer[2])
                    if choice2 != ca_answer[2]:
                        easygui.msgbox("Sorry that was incorrect", TITLE)
                        easygui.msgbox("The answer was " + ca_answer[2], TITLE)
                        answers += 1
                    if choice2 == ca_answer[2]:
                        easygui.msgbox("That was correct!", TITLE)
                        answers += 1
                if choice == ca_answer[2]:
                    easygui.msgbox("Well done! That was correct", TITLE)
                    answers += 1
                    score += 1
                # first attempt at question
                choice = easygui.buttonbox(question[3], TITLE, choices=answer[3])
                if choice != ca_answer[3]:
                    easygui.msgbox("Sorry that was incorrect. Try again", TITLE)
                    # second attempt at question
                    choice2 = easygui.buttonbox(question[3], TITLE, choices=answer[3])
                    if choice2 != ca_answer[3]:
                        easygui.msgbox("Sorry that was incorrect", TITLE)
                        easygui.msgbox("The answer was " + ca_answer[3], TITLE)
                        answers += 1
                    if choice2 == ca_answer[3]:
                        easygui.msgbox("That was correct!", TITLE)
                        answers += 1
                if choice == ca_answer[3]:
                    easygui.msgbox("Well done! That was correct", TITLE)
                    answers += 1
                    score += 1
                # first attempt at question
                choice = easygui.buttonbox(question[4], TITLE, choices=answer[4])
                if choice != ca_answer[4]:
                    easygui.msgbox("Sorry that was incorrect. Try again", TITLE)
                    # second attempt at question
                    choice2 = easygui.buttonbox(question[4], TITLE, choices=answer[4])
                    if choice2 != ca_answer[4]:
                        easygui.msgbox("Sorry that was incorrect", TITLE)
                        easygui.msgbox("The answer was " + ca_answer[4], TITLE)
                        answers += 1
                    if choice2 == ca_answer[4]:
                        easygui.msgbox("That was correct!", TITLE)
                        answers += 1
                if choice == ca_answer[4]:
                    easygui.msgbox("Well done! That was correct", TITLE)
                    answers += 1
                    score += 1
            easygui.msgbox("Well done " + name + " you completed the quiz! You got " + str(score) + " out of 5", TITLE)
        # changes what the quiz is about depending on the users choice
        if subject == "Science":
            quiz("Science", Q_SCIENCE, CA_SCIENCE, A_SCIENCE)
            answers = 5
        if subject == "Math":
            quiz("Math", Q_MATH, CA_MATH, A_MATH)
            answers = 5
        if subject == "History":
            quiz("History", Q_HISTORY, CA_HISTORY, A_HISTORY)
            answers = 5
        if subject == "Geography":
            quiz("Geography", Q_GEO, CA_GEO, A_GEO)
            answers = 5
        if subject == "Riddles":
            quiz("Riddles", Q_RIDDLES, CA_RIDDLES, A_RIDDLES)
            answers = 5
        if subject == "General":
            quiz("General", Q_GENERAL, CA_GENERAL, A_GENERAL)
            answers = 5
    # only runs this code once the user has answered all the questions
    while answers == 5:
        # play again feature that gives users the choice to go again or quit
        PLAY_AGAIN = easygui.buttonbox("Would you like to play again?", TITLE, choices=["Yes", "No"])  
        # runs when the user doesn't want to play again
        if PLAY_AGAIN == "No":
            easygui.msgbox("Goodbye " + name, TITLE)
            fun = easygui.buttonbox("Did you have fun?", TITLE, choices=["Yes","No"])
            if fun == "Yes":
               easygui.msgbox("I'm glad :D. I hope you come back " + name, TITLE)
            if fun == "No":
                easygui.msgbox("Oh.", TITLE)
            break
        # runs when the user does want to play again
        if PLAY_AGAIN == "Yes":
            easygui.msgbox("Lets play!")
            # resets everything so that the code will run again
            answers = 0
            score = 0
# if the user is above or below the allocated age range
if age >= MAX_AGE or age <= MIN_AGE:  
    easygui.msgbox("You are not old enough to play", TITLE)
