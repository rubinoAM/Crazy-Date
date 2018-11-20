# Clear Function
import os
def clear_ui():
    input("Please press enter to continue.")
    os.system("clear")

# Meet & Greet The Player
print ("Before we begin this little game of ours, I need to ask of you a small bit of information.")
player_name = input("What would happen to be your name? Or if you happen to dislike your actual name, what would you prefer I call you? > ")
print ("Ah, so %s is it? Fair enough." % (player_name))
print ("Let's begin this little charade, shall we?")
clear_ui()

# Introduction
print ("=========PROLOGUE=========")
print ("Ah, yet another day of tedious office work, bumper-to-bumper traffic, and aggravating superiors done with!")
print ("And, thank the sun, moon and stars, the weekend has finally arrived!")
print ("Normally a trip directly to the couch with your face buried in the cushions would be in order, followed summarily by a nap of some indeterminable length.")
print ("But today isn't an ordinary Friday how you see it.")
print ("Tonight's the night you finally get a chance to romance your lovely co-worker Belinda!")
print ("Admittedly, you tripped over your tongue a good dozen times before you finally managed to ask her out.")
print ("Actually, if I recall, she answered 'Yes' before you really finished your query.")
print ("It's just as well. To have your stammering speech read as charming to her certainly was a blessing.")
clear_ui()

# Questionnaire
answers = {
    "A":0,"B":0,"C":0,"D":0,"E":0,"X":0
}

print ("Now I have a questionnaire of sorts to run through with you.")
print ("Don't fret! No important information will be leaked into the wrong hands!")
print ("These questions are just to determine certain... aspects to tonight's events.")

# Gender
gender_choices = ["Male", "Female", "Androgynous"]

print("Oh good land! There was one last question I needed to ask. Please bear with me.")
print("What gender do you consider yourself? If you happen to be genderfluid, then what gender do you choose to present as tonight?")    
player_gender = input("Your choices are: Male, Female, Androgynous (Type them exactly as they are here!!) > ")

if(player_gender == "Male"):
    print("Male you say? Duly noted!")
elif(player_gender == "Female"):
    print("Female you say? Duly noted!")
elif(player_gender == "Androgynous"):
    print("Androgynous you say? Duly noted!")
else:
    print("Please choose one of the options provided.")

print ("Splendid. By the by, don't fret about how your date will feel about your gender.")
print ("This tale requires that our leading lady finds you attractive regardless of your gender.")
print ("Just make sure that your true personality attracts her as well.\n;^ )")
print("Well now that we have that last detail out of the way, we're off!")
clear_ui()

# Arrival
print("=========ACT 1: ARRIVAL=========")
print("The trip over to the restaurant certainly could've been... less hectic.")
print("Naturally you're kicking yourself for overlooking traffic density at this night.")
print("Easy mistake to make, I say.")
print("The incident with that ice cream van crashing into the library entrance...")
print("Well that bit isn't exactly easy to account for in one's itinery. I can give you that.")
print("Nor would it have been easy to predict a bear walking on two legs, wielding a shark as a club, and assaulting people.")
print("Nor that collision between that U.F.O. and your elderly neighbor's Cadillac Escalade on the 285.")
print("Of all the nights for your life to resemble that of a background character in an Adult Swim cartoon!")