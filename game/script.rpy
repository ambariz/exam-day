define t = Character("Teacher")
define f = Character("Friend")

default grades = 50
default energy = 50
default sanity = 50

label start:

    $ player_name = renpy.input("What is your name ?")
    $ player_name = player_name.strip()

    "Welcome, [player_name]!"
    "Today is the biggest exam of your life."

    jump choice_1

label choice_1:

    f "Trust me friend, studying is a mindset."

    menu:
        "What do you do?"
        "Study properly":
            $ grades += 10
            $ energy -= 5

        "Believe him":
            $ sanity -= 10

        "Play games instead":
            $ grades -= 10
            $ sanity += 5

    "Current Stats:"
    "Grades: [grades]"
    "Energy: [energy]"
    "Sanity: [sanity]"

    jump choice_2

label choice_2:

    "It's 10 PM."
    "You open YouTube for 'just one cartoon video'."
    f "Trust me friend, one cartoon won't reduce marks."

    menu:
        "What do you do?"
        "Go to sleep":
            $ sanity += 15
            $ energy += 5

        "Watch one cartoon":
            $ energy -= 5

        "Watch 20 videos":
            $ energy -= 20
            $ grades -= 10
            $ sanity += 10

    "Current Stats:"
    "Grades: [grades]"
    "Energy: [energy]"
    "Sanity: [sanity]"

    jump choice_3

    return

label choice_3:

    "Exam day has arrived"
    "You're about to leave for school."
    t "Did you eat breakfast?"

    menu:
        "What do you do?"
        "Eat a healthy breakfast":
            $ energy += 10
            $ grades += 5
        "Skip breakfast":
            $ energy -= 10
        "Drink only juice":
            $ energy += 5
            $ sanity -= 10
    "Grades: [grades]"
    "Energy: [energy]"
    "Sanity: [sanity]"
    jump choice_4
    return

label choice_4:

    "You sit down for the exam."
    f "Trust me friend, pick C for every answer."
    menu:
        "What do you do?"
        "Actually think about the answers":
            $ grade += 15
        "Pick C for everything":
            $ grades -= 15
            $ sanity += 5
        "Draw a smiley face on the paper"
            $ grades -= 25
            $ sanity += 5
    "Grades: [grades]"
    "Energy: [energy]"
    "Sanity: [sanity]"

    jump ending_check
    return
label ending_check:
    if grades >= 70:
        jump topper_ending
    elif energy >= 70:
        jump sleep_champion_ending
    elif sanity >= 70: 
        jump chaos_ending
    else:
        jump average_ending

label topper_ending:
    "You aced the exam!"
    "Your teachers are impressed"
    "TOPPER"
    return

label sleep_champion_ending:
    "You may not know every answer..."
    "But you got amazing sleep and peak health."
    "SLEEP CHAMPION ENDING"
    return  

label chaos_ending:
    "Nobody understands your exam paper."
    "Not even you :("
    "CHAOS ENDING"
    return  

label average_ending:
    "You somehow survived."
    "A pass is a pass."
    "AVERAGE STUDENT ENDING"
    return  
