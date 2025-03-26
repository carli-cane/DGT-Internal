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

A1_SCIENCE = ["Middle","Nucleus","Centre","Heart"]
A1_MATH = ["Triangle Formula", "Quadratic Equation", "Pythagoras Theorum", "Law of Gravity"]
A1_HISTORY = ["1940", "1921", "1948", "1939"]
A1_GEO =["New York", "Washington D.C", "Chicago", "Canada"]
A1_RIDDLES =["Sponge", "Bucket", "Mouth", "Wells"]
A1_GENERAL =["Flock", "Group", "Murder", "Fowl"]

A2_SCIENCE =["Carbon Dioxide", "Nitrogen", "Oxygen", "Carbon"]
A2_MATH =["180","100","80","90"]
A2_HISTORY =["ANZAC day","Memorial day", "Remembrance day","Victory day"]
A2_GEO =["Gulf of America","Gulf of Panama","Gulf of Mexico","Gulf of Oman"]
A2_RIDDLES =["Light","Darkness","Air","Speed"]
A2_GENERAL =["2","1","12","3"]

A3_SCIENCE =["Distance/Time", "Time/Distance", "Speed/Time","Distance/Speed"]
A3_MATH =["6","4","12","20"]
A3_HISTORY =["50","100","116","101"]
A3_GEO =["France","Italy","America","Romania"]
A3_RIDDLES =["Key ring","Piano","Fish","Doors"]
A3_GENERAL =["O+","-AB","-O","AB"]

A4_SCIENCE =["2", "1", "4", "5"]
A4_MATH =["32","68","44","64"]
A4_HISTORY =["1942", "1946","1945","1940"]
A4_GEO =["None","Brazil","France","United Kingdom"]
A4_RIDDLES =["Never","The dictionary","In the future","In the past"]
A4_GENERAL =["Ares","Demeter","Persephone","Aphrodite"]

A5_SCIENCE =["112","100","118","200"]
A5_MATH =["12","16","20","18"]
A5_HISTORY =["Neil Armstrong","John Glenn","Buzz Aldrin","Alan Shepard"]
A5_GEO =["Iceland","America","Canada","Denmark"]
A5_RIDDLES =["Missisipi", "A blind person","A potato","A key"]
A5_GENERAL =["Neptune","Uranus","Jupiter","Earth"]


easygui.msgbox("Welcome to the game", TITLE)
age = easygui.integerbox("Before we begin, how old are you?", TITLE)
if age > MIN_AGE and age < MAX_AGE:
   easygui.msgbox("You are old enough to play",TITLE)
PLAY_AGAIN = "Yes"
while PLAY_AGAIN == "Yes" and age > MIN_AGE and age < MAX_AGE:
    while ANSWER < 5:
      subject = easygui.buttonbox("What would you like to be quizzed on?", TITLE, SUBJECTS)
      for x in SUBJECTS[:]:
         if x == subject:
            SUBJECTS.remove(x)
      
      if subject == "Science":
         easygui.msgbox("Awesome! You will be answering science questions",TITLE)
         choice = easygui.buttonbox(Q_SCIENCE[0], TITLE, choices = A1_SCIENCE)
         if choice != CA_SCIENCE[0]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_SCIENCE[0], TITLE, choices = A1_SCIENCE)
            if choice2 != CA_SCIENCE[0]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_SCIENCE[0],TITLE)
               ANSWER += 1
            if choice2 == CA_SCIENCE[0]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_SCIENCE[0]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_SCIENCE[1], TITLE, choices = A2_SCIENCE)
         if choice != CA_SCIENCE[1]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_SCIENCE[1], TITLE, choices = A2_SCIENCE)
            if choice2 != CA_SCIENCE[1]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_SCIENCE[1],TITLE)
               ANSWER += 1
            if choice2 == CA_SCIENCE[1]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_SCIENCE[1]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_SCIENCE[2], TITLE, choices = A3_SCIENCE)
         if choice != CA_SCIENCE[2]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_SCIENCE[2], TITLE, choices = A3_SCIENCE)
            if choice2 != CA_SCIENCE[2]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_SCIENCE[2],TITLE)
               ANSWER += 1
            if choice2 == CA_SCIENCE[2]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_SCIENCE[2]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_SCIENCE[3], TITLE, choices = A4_SCIENCE)
         if choice != CA_SCIENCE[3]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_SCIENCE[3], TITLE, choices = A4_SCIENCE)
            if choice2 != CA_SCIENCE[3]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_SCIENCE[3],TITLE)
               ANSWER += 1
            if choice2 == CA_SCIENCE[3]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_SCIENCE[3]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_SCIENCE[4], TITLE, choices = A5_SCIENCE)
         if choice != CA_SCIENCE[4]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_SCIENCE[4], TITLE, choices = A5_SCIENCE)
            if choice2 != CA_SCIENCE[4]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_SCIENCE[4],TITLE)
               ANSWER += 1
            if choice2 == CA_SCIENCE[4]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_SCIENCE[4]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
      
      if subject == "Math":
         easygui.msgbox("Awesome! You will be answering math questions",TITLE)
         choice = easygui.buttonbox(Q_MATH[0], TITLE, choices = A1_MATH)
         if choice != CA_MATH[0]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_MATH[0], TITLE, choices = A1_MATH)
            if choice2 != CA_MATH[0]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_MATH[0],TITLE)
               ANSWER += 1
            if choice2 == CA_MATH[0]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_MATH[0]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_MATH[1], TITLE, choices = A2_MATH)
         if choice != CA_MATH[1]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_MATH[1], TITLE, choices = A2_MATH)
            if choice2 != CA_MATH[1]:
               easygui.msgbox("Sorry that was incorrect")
               easygui.msgbox("The answer was " + CA_MATH[1],TITLE)
               ANSWER += 1
            if choice2 == CA_MATH[1]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_MATH[1]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_MATH[2], TITLE, choices = A3_MATH)
         if choice != CA_MATH[2]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_MATH[2], TITLE, choices = A3_MATH)
            if choice2 != CA_MATH[2]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_MATH[2],TITLE)
               ANSWER += 1
            if choice2 == CA_MATH[2]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_MATH[2]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_MATH[3], TITLE, choices = A4_MATH)
         if choice != CA_MATH[3]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_MATH[3], TITLE, choices = A4_MATH)
            if choice2 != CA_MATH[3]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_MATH[3],TITLE)
               ANSWER += 1
            if choice2 == CA_MATH[3]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_MATH[3]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_MATH[4], TITLE, choices = A5_MATH)
         if choice != CA_MATH[4]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_MATH[4], TITLE, choices = A5_MATH)
            if choice2 != CA_MATH[4]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_MATH[4],TITLE)
               ANSWER += 1
            if choice2 == CA_MATH[4]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_MATH[4]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
               
      
      if subject == "History":
         easygui.msgbox("Awesome! You will be answering history questions",TITLE)
         choice = easygui.buttonbox(Q_HISTORY[0], TITLE, choices = A1_HISTORY)
         if choice != CA_HISTORY[0]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_HISTORY[0], TITLE, choices = A1_HISTORY)
            if choice2 != CA_HISTORY[0]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_HISTORY[0],TITLE)
               ANSWER += 1
            if choice2 == CA_HISTORY[0]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_HISTORY[0]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_HISTORY[1], TITLE, choices = A2_HISTORY)
         if choice != CA_HISTORY[1]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_HISTORY[1], TITLE, choices = A2_HISTORY)
            if choice2 != CA_HISTORY[1]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_HISTORY[1],TITLE)
               ANSWER += 1
            if choice2 == CA_HISTORY[1]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_HISTORY[1]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_HISTORY[2], TITLE, choices = A3_HISTORY)
         if choice != CA_HISTORY[2]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_HISTORY[2], TITLE, choices = A3_HISTORY)
            if choice2 != CA_HISTORY[2]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_HISTORY[2],TITLE)
               ANSWER += 1
            if choice2 == CA_HISTORY[2]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_HISTORY[2]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_HISTORY[3], TITLE, choices = A4_HISTORY)
         if choice != CA_HISTORY[3]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_HISTORY[3], TITLE, choices = A4_HISTORY)
            if choice2 != CA_HISTORY[3]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_HISTORY[3],TITLE)
               ANSWER += 1
            if choice2 == CA_HISTORY[3]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_HISTORY[3]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_HISTORY[4], TITLE, choices = A5_HISTORY)
         if choice != CA_HISTORY[4]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_HISTORY[4], TITLE, choices = A5_HISTORY)
            if choice2 != CA_HISTORY[4]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_HISTORY[4],TITLE)
               ANSWER += 1
            if choice2 == CA_HISTORY[4]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_HISTORY[4]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
      
      if subject == "Geography":
         easygui.msgbox("Awesome! You will be answering geography questions",TITLE)
         choice = easygui.buttonbox(Q_GEO[0], TITLE, choices = A1_GEO)
         if choice != CA_GEO[0]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_GEO[0], TITLE, choices = A1_GEO)
            if choice2 != CA_GEO[0]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_GEO[0],TITLE)
               ANSWER += 1
            if choice2 == CA_GEO[0]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_GEO[0]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_GEO[1], TITLE, choices = A2_GEO)
         if choice != CA_GEO[1]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_GEO[1], TITLE, choices = A2_GEO)
            if choice2 != CA_GEO[1]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_GEO[1],TITLE)
               ANSWER += 1
            if choice2 == CA_GEO[1]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_GEO[1]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_GEO[2], TITLE, choices = A3_GEO)
         if choice != CA_GEO[2]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_GEO[2], TITLE, choices = A3_GEO)
            if choice2 != CA_GEO[2]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_GEO[2],TITLE)
               ANSWER += 1
            if choice2 == CA_GEO[2]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_GEO[2]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_GEO[3], TITLE, choices = A4_GEO)
         if choice != CA_GEO[3]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_GEO[3], TITLE, choices = A4_GEO)
            if choice2 != CA_GEO[3]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_GEO[3])
               ANSWER += 1
            if choice2 == CA_GEO[3]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_GEO[3]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_GEO[4], TITLE, choices = A5_GEO)
         if choice != CA_GEO[4]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_GEO[4], TITLE, choices = A5_GEO)
            if choice2 != CA_GEO[4]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_GEO[4],TITLE)
               ANSWER += 1
            if choice2 == CA_GEO[4]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_GEO[4]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
      
      if subject == "Riddles":
         easygui.msgbox("Awesome! You will be answering riddles",TITLE)
         choice = easygui.buttonbox(Q_RIDDLES[0], TITLE, choices = A1_RIDDLES)
         if choice != CA_RIDDLES[0]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_RIDDLES[0], TITLE, choices = A1_RIDDLES)
            if choice2 != CA_RIDDLES[0]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_RIDDLES[0],TITLE)
               ANSWER += 1
            if choice2 == CA_RIDDLES[0]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_RIDDLES[0]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_RIDDLES[1], TITLE, choices = A2_RIDDLES)
         if choice != CA_RIDDLES[1]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_RIDDLES[1], TITLE, choices = A2_RIDDLES)
            if choice2 != CA_RIDDLES[1]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_RIDDLES[1],TITLE)
               ANSWER += 1
            if choice2 == CA_RIDDLES[1]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_RIDDLES[1]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_RIDDLES[2], TITLE, choices = A3_RIDDLES)
         if choice != CA_RIDDLES[2]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_RIDDLES[2], TITLE, choices = A3_RIDDLES)
            if choice2 != CA_RIDDLES[2]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_RIDDLES[2],TITLE)
               ANSWER += 1
            if choice2 == CA_RIDDLES[2]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_RIDDLES[2]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_RIDDLES[3], TITLE, choices = A4_RIDDLES)
         if choice != CA_RIDDLES[3]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_RIDDLES[3], TITLE, choices = A4_RIDDLES)
            if choice2 != CA_RIDDLES[3]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_RIDDLES[3],TITLE)
               ANSWER += 1
            if choice2 == CA_RIDDLES[3]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_RIDDLES[3]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_RIDDLES[4], TITLE, choices = A5_RIDDLES)
         if choice != CA_RIDDLES[4]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_RIDDLES[4], TITLE, choices = A5_RIDDLES)
            if choice2 != CA_RIDDLES[4]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_RIDDLES[4], TITLE)
               ANSWER += 1
            if choice2 == CA_RIDDLES[4]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_RIDDLES[4]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
   
      
      if subject == "General":
         easygui.msgbox("Awesome! You will be answering general  questions",TITLE)
         choice = easygui.buttonbox(Q_GENERAL[0],TITLE, choices = A1_GENERAL)
         if choice != CA_GENERAL[0]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_GENERAL[0],TITLE, choices = A1_GENERAL)
            if choice2 != CA_GENERAL[0]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_GENERAL[0],TITLE)
               ANSWER += 1
            if choice2 == CA_GENERAL[0]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_GENERAL[0]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_GENERAL[1],TITLE, choices = A2_GENERAL)
         if choice != CA_GENERAL[1]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_GENERAL[1],TITLE, choices = A2_GENERAL)
            if choice2 != CA_GENERAL[1]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_GENERAL[1],TITLE)
               ANSWER += 1
            if choice2 == CA_GENERAL[1]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_GENERAL[1]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_GENERAL[2],TITLE, choices = A3_GENERAL)
         if choice != CA_GENERAL[2]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_GENERAL[2],TITLE, choices = A3_GENERAL)
            if choice2 != CA_GENERAL[2]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_GENERAL[2],TITLE)
               ANSWER += 1
            if choice2 == CA_GENERAL[2]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_GENERAL[2]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_GENERAL[3],TITLE, choices = A4_GENERAL)
         if choice != CA_GENERAL[3]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_GENERAL[3],TITLE, choices = A4_GENERAL)
            if choice2 != CA_GENERAL[3]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_GENERAL[3],TITLE)
               ANSWER += 1
            if choice2 == CA_GENERAL[3]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_GENERAL[3]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
         choice = easygui.buttonbox(Q_GENERAL[4], TITLE, choices = A5_GENERAL)
         if choice != CA_GENERAL[4]:
            easygui.msgbox("Sorry that was incorrect. Try again",TITLE)
            choice2 = easygui.buttonbox(Q_GENERAL[4], TITLE, choices = A5_GENERAL)
            if choice2 != CA_GENERAL[4]:
               easygui.msgbox("Sorry that was incorrect",TITLE)
               easygui.msgbox("The answer was " + CA_GENERAL[4])
               ANSWER += 1
            if choice2 == CA_GENERAL[4]:
               easygui.msgbox("That was correct!",TITLE)
               ANSWER += 1
         if choice == CA_GENERAL[4]:
            easygui.msgbox("Well done! That was correct",TITLE)
            ANSWER += 1
            SCORE +=1
    while ANSWER == 5:
      easygui.msgbox("Well done you completed the quiz! You got " + str(SCORE) + " out of 5",TITLE)
      PLAY_AGAIN = easygui.buttonbox("Would you like to play again?",TITLE,choices = ["Yes","No"])
      if PLAY_AGAIN == "No":
         easygui.msgbox("Goodbye", TITLE)
         break  
      if PLAY_AGAIN == "Yes":
         easygui.msgbox("Lets play!")
         ANSWER = 0
         SCORE = 0
         
if age >= MAX_AGE or age <= MIN_AGE:
   easygui.msgbox("You are not old enough to play", TITLE)
