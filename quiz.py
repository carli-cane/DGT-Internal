import easygui 
TITLE = "Carli's Quiz"
SCORE = 0 #how many they get right
ANSWER = 0 #how many they've answered
SUBJECTS = ["Science", "Math", "History", "Geography", "Riddles", "General"]
Q_SCIENCE = ["What is the center of an atom called?", "What gas makes up most of our atomsphere?", "Which one of these is the correct formula for speed?","How many chambers does the human heart have?", "How many elements are there on the periodic table?"]
Q_MATH = ["What is the name of this formula 'A^2 + B^2 = C^2'", "How many degress is a right angle?", "What is the highest common factor (HCF) of 60 and 40?", "What is 16 x 4?","If x + 10 = 28 what is the value of x?"]
Q_HISTORY = ["What year did World War 2 start?","What day is a memorial day for soldiers in New Zealand and Australia?", "How many years did the 100 year war last?","What year did Hitler commit suicide?","Who was the first person on the moon?"]
Q_GEO = ["What is the capital of the United States of America?", "Which gulf recently had its name changed?", "What country is the Leaning Tower of Pisa in?", "Which country has a replica of the Statue of Liberty?", "What country is the closest to Greenland?"]
Q_RIDDLES = ["What is full of holes but still holds water?","The more there is, the less you see. What is it?","What has many keys but cannot open any doors?", "Where does today come before yesterday?","What has lots of eyes but cannot see?"]
Q_GENERAL = ["What is a group of crows called?", "How many hearts does an octopus have?","What is the rarest blood tyep?","Who is the greek god or goddess of love?","What is the only planet that rotates on its side?"]
CA_SCIENCE = ["Nucleus", "Nitrogen", "Distance/Time", "4","118"]
CA_MATH = ["Pythagoras Theorum", "90","20","64","18"]
CA_HISTORY = ["1939","ANZAC","1945","116","Neil Armstrong"]
CA_GEO = ["Washington D.C", "Gulf of Mexico","Italy","France","Canada"]
CA_RIDDLES = ["Sponge","Darkness","Piano","The dictionary", "A potato"]
CA_GENERAL = ["Murder","3","-AB","Aphrodite","Uranus"]

A1_SCIENCE = ["Middle","Nucleus","Centre","Heart"]
A1_MATH = ["Triangle Formula", "Quadratic Equation", "Pythagoras Theorum", "Law of Gravity"]
A1_HISTORY = ["1940", "1921", "1948", "1939"]
A1_GEO =["New York", "Washington D.C", "Chicago", "Canada"]
A1_RIDDLES =["Sponge", "Bucket", "Mouth", "Wells"]
A1_GENERAL =["Flock", "Group", "Murder", "Fowl"]

A2_SCIENCE =[]
A2_MATH =[]
A2_HISTORY =[]
A2_GEO =[]
A2_RIDDLES =[]
A2_GENERAL =[]

A3_SCIENCE =[]
A3_MATH =[]
A3_HISTORY =[]
A3_GEO =[]
A3_RIDDLES =[]
A3_GENERAL =[]

A4_SCIENCE =[]
A4_MATH =[]
A4_HISTORY =[]
A4_GEO =[]
A4_RIDDLES =[]
A4_GENERAL =[]

A5_SCIENCE =[]
A5_MATH =[]
A5_HISTORY =[]
A5_GEO =[]
A5_RIDDLES =[]
A5_GENERAL =[]


easygui.msgbox("Welcome to the game", TITLE)
age = easygui.integerbox("Before we begin, how old are you?", TITLE)
if age < 18 or age > 14:
   subject = easygui.buttonbox("What would you like to be quized on?", TITLE, SUBJECTS)
   
   if subject == "Science":
      easygui.msgbox("Awesome! You will be answering science questions",TITLE)
      choice = easygui.buttonbox(Q_SCIENCE[0], TITLE, choices = A1_SCIENCE)
      if choice != CA_SCIENCE[0]:
         easygui.msgbox("Sorry that was incorrect. Try again")
         choice2 = easygui.buttonbox(Q_SCIENCE[0], TITLE, choices = A1_SCIENCE)
         if choice2 != CA_SCIENCE[0]:
            easygui.msgbox("Sorry that was incorrect")
            easygui.msgbox("The answer was " + CA_SCIENCE[0])
            ANSWER += 1
         if choice2!= CA_SCIENCE[0]:
            easygui.msgbox("That was correct!")
            ANSWER += 1
      if choice == CA_SCIENCE[0]:
         easygui.msgbox("Well done! That was correct")
         ANSWER += 1
         SCORE +=1
   
   if subject == "Math":
      easygui.msgbox("Awesome! You will be answering math questions",TITLE)
      choice = easygui.buttonbox(Q_MATH[0], TITLE, choices = A1_MATH)
      if choice != CA_MATH[0]:
         easygui.msgbox("Sorry that was incorrect. Try again")
         choice2 = easygui.buttonbox(Q_MATH[0], TITLE, choices = A1_MATH)
         if choice2 != CA_MATH[0]:
            easygui.msgbox("Sorry that was incorrect")
            easygui.msgbox("The answer was " + CA_MATH[0])
            ANSWER += 1
         if choice2!= CA_MATH[0]:
            easygui.msgbox("That was correct!")
            ANSWER += 1
      if choice == CA_MATH[0]:
         easygui.msgbox("Well done! That was correct")
         ANSWER += 1
         SCORE +=1
            
   
   if subject == "History":
      easygui.msgbox("Awesome! You will be answering history questions",TITLE)
      choice = easygui.buttonbox(Q_HISTORY[0], TITLE, choices = A1_HISTORY)
      if choice != CA_HISTORY[0]:
         easygui.msgbox("Sorry that was incorrect. Try again")
         choice2 = easygui.buttonbox(Q_HISTORY[0], TITLE, choices = A1_HISTORY)
         if choice2 != CA_HISTORY[0]:
            easygui.msgbox("Sorry that was incorrect")
            easygui.msgbox("The answer was " + CA_HISTORY[0])
            ANSWER += 1
         if choice2!= CA_HISTORY[0]:
            easygui.msgbox("That was correct!")
            ANSWER += 1
      if choice == CA_HISTORY[0]:
         easygui.msgbox("Well done! That was correct")
         ANSWER += 1
         SCORE +=1
   
   if subject == "Geography":
      easygui.msgbox("Awesome! You will be answering geography questions",TITLE)
      choice = easygui.buttonbox(Q_GEO[0], TITLE, choices = A1_GEO)
      if choice != CA_GEO[0]:
         easygui.msgbox("Sorry that was incorrect. Try again")
         choice2 = easygui.buttonbox(Q_GEO[0], TITLE, choices = A1_GEO)
         if choice2 != CA_GEO[0]:
            easygui.msgbox("Sorry that was incorrect")
            easygui.msgbox("The answer was " + CA_GEO[0])
            ANSWER += 1
         if choice2!= CA_GEO[0]:
            easygui.msgbox("That was correct!")
            ANSWER += 1
      if choice == CA_GEO[0]:
         easygui.msgbox("Well done! That was correct")
         ANSWER += 1
         SCORE +=1
   
   if subject == "Riddles":
      easygui.msgbox("Awesome! You will be answering riddles",TITLE)
      choice = easygui.buttonbox(Q_RIDDLES[0], TITLE, choices = A1_RIDDLES)
      if choice != CA_RIDDLES[0]:
         easygui.msgbox("Sorry that was incorrect. Try again")
         choice2 = easygui.buttonbox(Q_RIDDLES[0], TITLE, choices = A1_RIDDLES)
         if choice2 != CA_RIDDLES[0]:
            easygui.msgbox("Sorry that was incorrect")
            easygui.msgbox("The answer was " + CA_RIDDLES[0])
            ANSWER += 1
         if choice2!= CA_RIDDLES[0]:
            easygui.msgbox("That was correct!")
            ANSWER += 1
      if choice == CA_RIDDLES[0]:
         easygui.msgbox("Well done! That was correct")
         ANSWER += 1
         SCORE +=1
   
   if subject == "General":
      easygui.msgbox("Awesome! You will be answering general  questions",TITLE)
      choice = easygui.buttonbox(Q_GENERAL[0], TITLE, choices = A1_GENERAL)
      if choice != CA_GENERAL[0]:
         easygui.msgbox("Sorry that was incorrect. Try again")
         choice2 = easygui.buttonbox(Q_GENERAL[0], TITLE, choices = A1_GENERAL)
         if choice2 != CA_GENERAL[0]:
            easygui.msgbox("Sorry that was incorrect")
            easygui.msgbox("The answer was " + CA_GENERAL[0])
            ANSWER += 1
         if choice2!= CA_GENERAL[0]:
            easygui.msgbox("That was correct!")
            ANSWER += 1
      if choice == CA_GENERAL[0]:
         easygui.msgbox("Well done! That was correct")
         ANSWER += 1
         SCORE +=1

if age > 18 or age < 14:
   easygui.msgbox("You are not old enough to play")
