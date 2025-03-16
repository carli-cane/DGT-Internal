import easygui 
TITLE = "Carli's Quiz"
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

easygui.msgbox("Welcome to the game", TITLE)
age = easygui.integerbox("Before we begin, how old are you?", TITLE)
if age < 18 or age > 14:
   subject = easygui.buttonbox("What would you like to be quized on?", TITLE, SUBJECTS)
   if subject == "Science":
      easygui.msgbox("Awesome! You will be answering science questions",TITLE)
   if subject == "Math":
      easygui.msgbox("Awesome! You will be answering math questions",TITLE)
   if subject == "History":
      easygui.msgbox("Awesome! You will be answering history questions",TITLE)
   if subject == "Geography":
      easygui.msgbox("Awesome! You will be answering geography questions",TITLE)
   if subject == "Riddles":
      easygui.msgbox("Awesome! You will be answering riddles",TITLE)
   if subject == "General":
      easygui.msgbox("Awesome! You will be answering general  questions",TITLE)
if age > 19 or age < 14:
   easygui.msgbox("You are not old enough to play")
