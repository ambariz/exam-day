define t = Character("Teacher")
define f = Character("Friend")

default grades = 50
default energy = 50
default sanity = 50

default persistent.topper = "Locked"
default persistent.sleep = "Locked"
default persistent.chaos = "Locked"
default persistent.average = "Locked" 

image bedroom:
    "assets/bg/bedroom.jpeg"
    zoom 3.4

image class_room:
    "assets/bg/class_room.jpg"
    zoom 2

image exam_hall:
    "assets/bg/exam_hall.avif"
    zoom 0.7

image topper:
    "assets/bg/topper.avif"
    zoom 2.59

label start:

    scene bedroom
    with fade 

    play music "assets/sounds/bgm.mp3" fadein 1.0 loop

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

        "What next?"
        "View Ending Collection":
            jump ending_gallery
        "Quit":
            return

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

        "What next?"
        "View Ending Collection":
            jump ending_gallery
        "Quit":
            return

    "Current Stats:"
    "Grades: [grades]"
    "Energy: [energy]"
    "Sanity: [sanity]"

    jump choice_3

    return

label choice_3:
    scene class_room
    with fade 

    "Exam day has arrived"

    stop music fadeout 1.0
    play music "assets/sounds/climax.mp3" fadein 1.0

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

        "What next?"
        "View Ending Collection":
            jump ending_gallery
        "Quit":
            return

    "Grades: [grades]"
    "Energy: [energy]"
    "Sanity: [sanity]"
    jump choice_4
    return

label choice_4:
    scene exam_hall
    with fade

    "You sit down for the exam."
    f "Trust me friend, pick C for every answer."
    menu:
        "What do you do?"
        "Actually think about the answers":
            $ grades += 15
        "Pick C for everything":
            $ grades -= 15
            $ sanity += 5
        "Draw a smiley face on the paper":
            $ grades -= 25
            $ sanity += 5

        "What next?"
        "View Ending Collection":
            jump ending_gallery
        "Quit":
            return
    stop music fadeout 1.0
    play music "assets/sounds/bgm.mp3" fadein 1.0

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
    scene topper
    with fade 
    $ persistent.topper = "Unlocked"
    "You aced the exam!"
    "Your teachers are impressed"
    "YOU ARE A TOPPER"
    return

label sleep_champion_ending:
    $ persistent.sleep = "Unlocked"
    "You may not know every answer..."
    "But you got amazing sleep and peak health."
    "YOU ARE A SLEEP CHAMPION"
    return  

label chaos_ending:
    $ persistent.chaos = "Unlocked"
    "Nobody understands your exam paper."
    "Not even you :("
    "YOU ARE A CHAOS KID"
    return  

label average_ending:
    $ persistent.average = "Unlocked"
    "You somehow survived."
    "A pass is a pass."
    "YOU ARE A BEST AVERAGE STUDENT"
    return  

label ending_gallery:
    "Unlocked Endings"

    "Topper: [persistent.topper]"
    "Sleep Champion: [persistent.sleep]"
    "Chaos: [persistent.chaos]"
    "Average: [persistent.average]"

    return


