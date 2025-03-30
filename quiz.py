import easygui
TITLE = "Carli's Quiz"
SCORE = 0 # how many they get right
ANSWER = 0 # how many they've answered
MIN_AGE = 14
MAX_AGE = 18
SUBJECTS = ["Science", "Math", "History", "Geography", "Riddles", "General"]
Q_SCIENCE = ["What is the center of an atom called?", "What gas makes up most of our atomsphere?", "Which one of these is the correct formula for speed?","How many chambers does the human heart have?", "How many elements are there on the periodic table?"]
Q_MATH = ["What is the name of this formula 'A^2 + B^2 = C^2'", "How many degress is a right angle?", "What is the highest common factor (HCF) of 60 and 40?", "What is 16 x 4?","If x + 10 = 28 what is the value of x?"]
Q_HISTORY = ["What year did World War 2 start?","What day is a memorial day for soldiers in New Zealand and Australia?", "How many years did the 100 year war last?","What year did Hitler commit suicide?","Who was the first person on the moon?"]
Q_GEO = ["What is the capital of the United States of America?", "Which gulf recently had its name changed?", "What country is the Leaning Tower of Pisa in?", "Which country has a replica of the Statue of Liberty?", "What country is the closest to Greenland?"]
Q_RIDDLES = ["What is full of holes but still holds water?","The more there is, the less you see. What is it?","What has many keys but cannot open any doors?", "Where does today come before yesterday?","What has lots of eyes but cannot see?"]
Q_GENERAL = ["What is a group of crows called?", "How many hearts does an octopus have?","What is the rarest blood type?","Who is the greek god or goddess of love?","What is the only planet that rotates on its side?"]

CA_SCIENCE = ["Nucleus", "Nitrogen", "Distance/Time", "4","118"]
CA_MATH = ["Pythagoras Theorum", "90","20","64","18"]
CA_HISTORY = ["1939","ANZAC day","116","1945","Neil Armstrong"]
CA_GEO = ["Washington D.C", "Gulf of Mexico","Italy","France","Canada"]
CA_RIDDLES = ["Sponge","Darkness","Piano","The dictionary", "A potato"]
CA_GENERAL = ["Murder","3","-AB","Aphrodite","Uranus"]

A_SCIENCE = [["Middle","Nucleus","Centre","Heart"],["Carbon Dioxide", "Nitrogen", "Oxygen", "Carbon"],["Distance/Time", "Time/Distance", "Speed/Time","Distance/Speed"],["2", "1", "4", "5"],["112","100","118","200"]]
A_MATH = [["Triangle Formula", "Quadratic Equation", "Pythagoras Theorum", "Law of Gravity"],["180","100","80","90"],["6","4","12","20"],["32","68","44","64"],["12","16","20","18"]]
A_HISTORY = [["1940", "1921", "1948", "1939"],["ANZAC day","Memorial day", "Remembrance day","Victory day"],["50","100","116","101"],["1942", "1946","1945","1940"],["Neil Armstrong","John Glenn","Buzz Aldrin","Alan Shepard"]]
A_GEO =[["New York", "Washington D.C", "Chicago", "Canada"],["Gulf of America","Gulf of Panama","Gulf of Mexico","Gulf of Oman"],["France","Italy","America","Romania"],["None","Brazil","France","United Kingdom"],["Iceland","America","Canada","Denmark"]]
A_RIDDLES =[["Sponge", "Bucket", "Mouth", "Wells"],["Light","Darkness","Air","Speed"],["Key ring","Piano","Fish","Doors"],["Never","The dictionary","In the future","In the past"],["Missisipi", "A blind person","A potato","A key"]]
A_GENERAL =[["Flock", "Group", "Murder", "Fowl"],["2","1","12","3"],["O+","-AB","-O","AB"],["Ares","Demeter","Persephone","Aphrodite"],["Neptune","Uranus","Jupiter","Earth"]]

easygui.msgbox("Welcome to the game", TITLE)
age = easygui.integerbox("Before we begin, how old are you?", TITLE)
if age > MIN_AGE and age < MAX_AGE:
   easygui.msgbox("You are old enough to play",TITLE)
name = easygui.enterbox("What is your name?",TITLE)
easygui.msgbox("Welcome " + name, TITLE)
PLAY_AGAIN = "Yes"
while PLAY_AGAIN == "Yes" and age > MIN_AGE and age < MAX_AGE:
   while ANSWER < 5:
      subject = easygui.buttonbox("What would you like to be quizzed on?", TITLE, SUBJECTS)
      for x in SUBJECTS[:]:
         if x == subject:
            SUBJECTS.remove(x)

      def quiz(subject,question, ca_answer, answer):
         SCORE = 0 # how many they get right
         ANSWER = 0 # how many they've answered
         while ANSWER < 5:
            easygui.msgbox("Awesome! You will be answering " + subject + " questions",TITLE)
            choice = easygui.buttonbox(question[0], TITLE, choices = answer[0])
            if choice != ca_answer[0]:
               easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
               choice2 = easygui.buttonbox(question[0], TITLE, choices = answer[0])
               if choice2 != ca_answer[0]:
                  easygui.msgbox("Sorry that was incorrect",TITLE)
                  easygui.msgbox("The answer was " + ca_answer[0],TITLE)
                  ANSWER += 1
               if choice2 == ca_answer[0]:
                  easygui.msgbox("That was correct!",TITLE)
                  ANSWER += 1
            if choice == ca_answer[0]:
               easygui.msgbox("Well done! That was correct",TITLE)
               ANSWER += 1
               SCORE +=1
            choice = easygui.buttonbox(question[1], TITLE, choices = answer[1])
            if choice != ca_answer[1]:
               easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
               choice2 = easygui.buttonbox(question[1], TITLE, choices = answer[1])
               if choice2 != ca_answer[1]:
                  easygui.msgbox("Sorry that was incorrect",TITLE)
                  easygui.msgbox("The answer was " + ca_answer[1],TITLE)
                  ANSWER += 1
               if choice2 == ca_answer[1]:
                  easygui.msgbox("That was correct!",TITLE)
                  ANSWER += 1
            if choice == ca_answer[1]:
               easygui.msgbox("Well done! That was correct",TITLE)
               ANSWER += 1
               SCORE +=1
            choice = easygui.buttonbox(question[2], TITLE, choices = answer[2])
            if choice != ca_answer[2]:
               easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
               choice2 = easygui.buttonbox(question[2], TITLE, choices = answer[2])
               if choice2 != ca_answer[2]:
                  easygui.msgbox("Sorry that was incorrect",TITLE)
                  easygui.msgbox("The answer was " + ca_answer[2],TITLE)
                  ANSWER += 1
               if choice2 == ca_answer[2]:
                  easygui.msgbox("That was correct!",TITLE)
                  ANSWER += 1
            if choice == ca_answer[2]:
               easygui.msgbox("Well done! That was correct",TITLE)
               ANSWER += 1
               SCORE +=1
            choice = easygui.buttonbox(question[3], TITLE, choices = answer[3])
            if choice != ca_answer[3]:
               easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
               choice2 = easygui.buttonbox(question[3], TITLE, choices = answer[3])
               if choice2 != ca_answer[3]:
                  easygui.msgbox("Sorry that was incorrect",TITLE)
                  easygui.msgbox("The answer was " + ca_answer[3],TITLE)
                  ANSWER += 1
               if choice2 == ca_answer[3]:
                  easygui.msgbox("That was correct!",TITLE)
                  ANSWER += 1
            if choice == ca_answer[3]:
               easygui.msgbox("Well done! That was correct",TITLE)
               ANSWER += 1
               SCORE +=1
            choice = easygui.buttonbox(question[4], TITLE, choices = answer[4])
            if choice != ca_answer[4]:
               easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
               choice2 = easygui.buttonbox(question[4], TITLE, choices = answer[4])
               if choice2 != ca_answer[4]:
                  easygui.msgbox("Sorry that was incorrect",TITLE)
                  easygui.msgbox("The answer was " + ca_answer[4],TITLE)
                  ANSWER += 1
               if choice2 == ca_answer[4]:
                  easygui.msgbox("That was correct!",TITLE)
                  ANSWER += 1
            if choice == ca_answer[4]:
               easygui.msgbox("Well done! That was correct",TITLE)
               ANSWER += 1
               SCORE +=1
         easygui.msgbox("Well done " + name + " you completed the quiz! You got " + str(SCORE) + " out of 5" ,TITLE)

      if subject == "Science":
         quiz("Science",Q_SCIENCE,CA_SCIENCE, A_SCIENCE)
         ANSWER = 5
      if subject == "Math":
         quiz("Math",Q_MATH,CA_MATH, A_MATH)
         ANSWER = 5
      if subject == "History":
         quiz("History", Q_HISTORY,CA_HISTORY,A_HISTORY)
         ANSWER = 5
      if subject == "Geography":
         quiz("Geography",Q_GEO,CA_GEO, A_GEO)
         ANSWER = 5
      if subject == "Riddles":
         quiz("Riddles",Q_RIDDLES,CA_RIDDLES, A_RIDDLES)
         ANSWER = 5
      if subject == "General":
         quiz("General",Q_GENERAL,CA_GENERAL, A_GENERAL)
         ANSWER = 5
         
   while ANSWER == 5:
      PLAY_AGAIN = easygui.buttonbox("Would you like to play again?",TITLE,choices = ["Yes","No"])
      if PLAY_AGAIN == "No":
         easygui.msgbox("Goodbye " + name, TITLE)
         break  
      if PLAY_AGAIN == "Yes":
         easygui.msgbox("Lets play!")
         ANSWER = 0
         SCORE = 0
         

if age >= MAX_AGE or age <= MIN_AGE:
   easygui.msgbox("You are not old enough to play", TITLE)
