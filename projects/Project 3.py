# Importing random module
import random
#def variables
choice = 1
choice2 = ""
# Defining list of phrases which will help to build a story
Sentence_starter = ['About 100 years ago','About 1,000 years ago','About 10,000 years ago','About 100,000 years ago',
                    'In the 20 BC','In the 200 BC','In the 20 AD','In the 400 AD', 'Once upon a time']
character = [' there lived a king.',' there lived an Emperor.',' there lived a Queen.',' there lived an Empress.', 
            ' there was a man named Jack.', ' there was a man named John.', 'there lived a farmer.', ' there lived a architect.', 
            ' there lived a bartender.', ' there lived a blacksmith.']
time = ['One day', 'One full-moon night']
story_plot = [' he was passing by',' he was going for a picnic to ']
place = [' the mountains of Kaldor', 'the garden of Algon', 'the valley of reason','the trench of truth','the abyss of Karthon',' the giant orb of destiny',]
second_character = [' they saw a man', ' they saw a young lady', ' they saw a troll',' they saw a giant bear',' they saw a dragon',' they saw a monk',]
age = [' who seemed to be young and eager to take on any challenge', ' who seemed very old and feeble']
work = [' searching something.', ' digging a well on roadside.', ' doing research.', ' destroying cities.', ' sleeping.',]

# Initial selection of an item from each list and concatenating them.
print(random.choice(Sentence_starter)+random.choice(character)+
        random.choice(time)+random.choice(story_plot)+
        random.choice(place)+random.choice(second_character)+
        random.choice(age)+random.choice(work)),
print(random.choice(Sentence_starter)+random.choice(character)+
        random.choice(time)+random.choice(story_plot)+ 
        random.choice(place)+random.choice(second_character)+ 
        random.choice(age)+random.choice(work)),
choice2 = input("which story did you like more? first? or second? "),
choice2 = str(choice2)
print("I also liked the " + choice2 + "!"),
#While loop to give user the choice to get another random story
while(choice < 2):
    choice = int(input("would you like another story? Only enter 1 for yes and 2 for no: "))
    choice2 = ""
# If Else statement so that they can get as many stories as they want so long as they choose to continue
    if choice == 1:
        print(random.choice(Sentence_starter)+random.choice(character)+
            random.choice(time)+random.choice(story_plot)+
            random.choice(place)+random.choice(second_character)+
            random.choice(age)+random.choice(work)),
        print(random.choice(Sentence_starter)+random.choice(character)+
            random.choice(time)+random.choice(story_plot)+ 
            random.choice(place)+random.choice(second_character)+ 
            random.choice(age)+random.choice(work)),
        choice2 = input("which story did you like more? first? or second? "),
        choice2 = str(choice2)
        print( "I liked the " + choice2 + " aswell! "),
    else:
        print("Thank you for reading my stories. Ihope you had some fun!")
